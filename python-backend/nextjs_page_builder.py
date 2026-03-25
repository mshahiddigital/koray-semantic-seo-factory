# nextjs_page_builder.py - Next.js MDX Page Generator
# Usage: python nextjs_page_builder.py --payload "page_payload.json" --output_dir "src/app"
# Usage: python nextjs_page_builder.py --batch "batch_payload.json" --output_dir "src/app"
# Outputs: MDX files in Next.js App Router format + a deployment manifest
#
# Targets: Next.js 14+ App Router with MDX support
# Schema: injected as <Script> tag in page metadata
# Compatible with: Contentlayer, next-mdx-remote, @next/mdx

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Slug utilities
# ---------------------------------------------------------------------------

def to_slug(text: str) -> str:
    """Convert title to URL-safe slug."""
    slug = text.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


# ---------------------------------------------------------------------------
# MDX frontmatter builder
# ---------------------------------------------------------------------------

def build_frontmatter(page: dict) -> str:
    """Build MDX frontmatter block for Next.js metadata API."""
    title = page.get("title", "")
    meta_description = page.get("meta_description", "")
    seo_title = page.get("seo_title", title)
    canonical = page.get("canonical_url", "")
    date_published = page.get("date_published", datetime.now().strftime("%Y-%m-%d"))
    date_modified = page.get("date_modified", date_published)
    og_image = page.get("og_image", "")
    author = page.get("author", "")
    tags = page.get("tags", [])
    focus_keyword = page.get("focus_keyword", "")

    lines = [
        "---",
        f'title: "{seo_title}"',
        f'description: "{meta_description}"',
        f'publishedAt: "{date_published}"',
        f'updatedAt: "{date_modified}"',
    ]
    if canonical:
        lines.append(f'canonical: "{canonical}"')
    if og_image:
        lines.append(f'image: "{og_image}"')
    if author:
        lines.append(f'author: "{author}"')
    if focus_keyword:
        lines.append(f'focusKeyword: "{focus_keyword}"')
    if tags:
        lines.append(f"tags: {json.dumps(tags)}")
    lines.append("---")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Schema injection for Next.js
# ---------------------------------------------------------------------------

def build_schema_script(schema_json: dict | list) -> str:
    """Build a Next.js <Script> component with JSON-LD schema.

    Uses dangerouslySetInnerHTML pattern required for JSON-LD in Next.js App Router.
    """
    schema_str = json.dumps(schema_json, indent=2, ensure_ascii=False)
    # Escape backticks for template literal safety
    schema_str = schema_str.replace("`", "\\`")

    return f"""<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{{{
    __html: JSON.stringify({json.dumps(schema_json, ensure_ascii=False)})
  }}}}
/>"""


# ---------------------------------------------------------------------------
# Internal link injector
# ---------------------------------------------------------------------------

def inject_internal_links_mdx(content: str, link_map: dict) -> str:
    """Replace anchor text in MDX content with Markdown hyperlinks."""
    for anchor_text, url in link_map.items():
        # Skip if already linked
        if f"[{anchor_text}]" in content:
            continue
        # Replace first occurrence, not inside code blocks
        pattern = r'(?<!\[)' + re.escape(anchor_text) + r'(?!\])'
        replacement = f"[{anchor_text}]({url})"
        content = re.sub(pattern, replacement, content, count=1)
    return content


# ---------------------------------------------------------------------------
# Page builder for App Router (page.mdx format)
# ---------------------------------------------------------------------------

def build_page_mdx(page: dict, deployed_slugs: dict) -> tuple[str, str]:
    """Build a complete MDX file for a single page.

    Returns: (relative_file_path, file_content)
    """
    title = page.get("title", "Untitled")
    slug = page.get("slug", to_slug(title))
    content_markdown = page.get("content_markdown", page.get("content_html", ""))
    schema_json = page.get("schema_json")
    internal_links = page.get("internal_links", {})
    parent_slug = page.get("parent_slug", "")

    # Inject internal links from both explicit map and deployed pages
    merged_links = {**deployed_slugs, **internal_links}
    if merged_links:
        content_markdown = inject_internal_links_mdx(content_markdown, merged_links)

    # Build file path: App Router uses /slug/page.mdx OR /parent/slug/page.mdx
    if parent_slug:
        rel_path = f"{parent_slug}/{slug}/page.mdx"
    else:
        rel_path = f"{slug}/page.mdx"

    # Build file content
    sections = [build_frontmatter(page), ""]

    # Schema injection (before content, inside JSX scope)
    if schema_json:
        sections.append(build_schema_script(schema_json))
        sections.append("")

    # Main content
    sections.append(content_markdown)

    return rel_path, "\n".join(sections)


# ---------------------------------------------------------------------------
# Metadata file for Next.js generateMetadata
# ---------------------------------------------------------------------------

def build_metadata_ts(pages: list) -> str:
    """Generate a metadata map file for dynamic metadata in Next.js.

    Outputs: src/app/metadata-map.ts
    """
    entries = []
    for page in pages:
        slug = page.get("slug", to_slug(page.get("title", "")))
        entries.append(f"""  "{slug}": {{
    title: "{page.get('seo_title', page.get('title', ''))}",
    description: "{page.get('meta_description', '')}",
    canonical: "{page.get('canonical_url', '')}",
  }},""")

    return f"""// Auto-generated by nextjs_page_builder.py — do not edit manually
// Generated: {datetime.now().isoformat()}

export const metadataMap: Record<string, {{
  title: string;
  description: string;
  canonical: string;
}}> = {{
{chr(10).join(entries)}
}};
"""


# ---------------------------------------------------------------------------
# Deployment manifest
# ---------------------------------------------------------------------------

def build_manifest(pages: list, output_dir: str) -> dict:
    """Build a deployment manifest of all created files."""
    return {
        "generated_at": datetime.now().isoformat(),
        "output_dir": output_dir,
        "total_pages": len(pages),
        "pages": [
            {
                "title": p.get("title"),
                "slug": p.get("slug", to_slug(p.get("title", ""))),
                "parent_slug": p.get("parent_slug", ""),
                "file": f"{p.get('parent_slug', '')}/{p.get('slug', to_slug(p.get('title', '')))}/page.mdx".lstrip("/"),
            }
            for p in pages
        ]
    }


# ---------------------------------------------------------------------------
# Main build function
# ---------------------------------------------------------------------------

def build_pages(pages: list, output_dir: str) -> dict:
    """Build all MDX pages and write to output_dir. Returns manifest."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    deployed_slugs = {}  # title → URL map built as pages are processed
    manifests = []

    for page in pages:
        title = page.get("title", "")
        slug = page.get("slug", to_slug(title))
        parent_slug = page.get("parent_slug", "")

        # Build URL for internal link map
        url_path = f"/{parent_slug}/{slug}" if parent_slug else f"/{slug}"
        deployed_slugs[title] = url_path

        # Build MDX
        rel_path, content = build_page_mdx(page, deployed_slugs)
        file_path = output_path / rel_path
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        manifests.append({
            "title": title,
            "slug": slug,
            "file": str(rel_path),
            "url": url_path,
            "status": "written",
        })
        print(f"Created: {rel_path}", file=sys.stderr)

    # Write metadata map
    metadata_ts = build_metadata_ts(pages)
    metadata_path = output_path / "metadata-map.ts"
    with open(metadata_path, "w", encoding="utf-8") as f:
        f.write(metadata_ts)
    print(f"Created: metadata-map.ts", file=sys.stderr)

    return {
        "status": "SUCCESS",
        "total": len(pages),
        "output_dir": output_dir,
        "pages": manifests,
        "metadata_map": str(metadata_path),
    }


# ---------------------------------------------------------------------------
# CLI interface
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Next.js MDX pages from SEO page payloads")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--payload", type=str, help="Single page payload JSON file")
    group.add_argument("--batch", type=str, help="Batch payload JSON file { pages: [...] }")
    parser.add_argument(
        "--output_dir", type=str, default="src/app",
        help="Root App Router directory (default: src/app)"
    )
    parser.add_argument("--manifest", type=str, default=None, help="Save manifest to JSON file")
    args = parser.parse_args()

    if args.payload:
        with open(args.payload, "r", encoding="utf-8") as f:
            payload = json.load(f)
        pages = [payload]
    else:
        with open(args.batch, "r", encoding="utf-8") as f:
            batch = json.load(f)
        pages = batch.get("pages", [])

    result = build_pages(pages, args.output_dir)
    output_json = json.dumps(result, indent=2, ensure_ascii=False)
    print(output_json)

    if args.manifest:
        with open(args.manifest, "w", encoding="utf-8") as f:
            f.write(output_json)
        print(f"Manifest saved to {args.manifest}", file=sys.stderr)

    sys.exit(0 if result["status"] == "SUCCESS" else 1)
