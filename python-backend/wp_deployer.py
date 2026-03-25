# wp_deployer.py - WordPress 6.9 REST API Deployment Script
# Usage: python wp_deployer.py --payload "page_payload.json" --credentials "wp_credentials.json"
# Outputs: JSON result { status, url, post_id, error }
#
# Authentication: WordPress Application Passwords (WP 5.6+)
# Set credentials in wp_credentials.json — never hardcode in this file.
#
# Required: pip install requests

import argparse
import json
import re
import sys
import requests
from requests.auth import HTTPBasicAuth


# ---------------------------------------------------------------------------
# Credential loader
# ---------------------------------------------------------------------------

def load_credentials(cred_path: str) -> dict:
    """Load WordPress credentials from JSON file.

    Expected format:
    {
        "wp_url": "https://yoursite.com",
        "wp_user": "admin",
        "wp_app_password": "xxxx xxxx xxxx xxxx xxxx xxxx"
    }
    """
    with open(cred_path, "r", encoding="utf-8") as f:
        creds = json.load(f)
    required = ["wp_url", "wp_user", "wp_app_password"]
    for key in required:
        if key not in creds:
            raise ValueError(f"Missing required credential field: {key}")
    # Strip trailing slash from URL
    creds["wp_url"] = creds["wp_url"].rstrip("/")
    return creds


# ---------------------------------------------------------------------------
# Internal link injector
# ---------------------------------------------------------------------------

def inject_internal_links(html_content: str, link_map: dict) -> str:
    """Replace anchor text in HTML with hyperlinks.

    link_map format: { "Anchor Text": "https://site.com/slug" }
    Matches are case-insensitive, whole-word, skips text already inside <a> tags.
    """
    for anchor_text, url in link_map.items():
        # Skip if already linked
        already_linked = re.search(
            r'<a[^>]*>' + re.escape(anchor_text) + r'</a>',
            html_content,
            re.IGNORECASE
        )
        if already_linked:
            continue
        # Replace first occurrence only (avoid over-linking)
        pattern = r'(?<!["\'>])(' + re.escape(anchor_text) + r')(?!["\'])'
        replacement = f'<a href="{url}">{anchor_text}</a>'
        html_content = re.sub(pattern, replacement, html_content, count=1, flags=re.IGNORECASE)
    return html_content


# ---------------------------------------------------------------------------
# Schema JSON-LD block builder
# ---------------------------------------------------------------------------

def build_schema_block(schema_json: dict) -> str:
    """Wrap schema dict in a <script> tag for head injection."""
    return f'<script type="application/ld+json">\n{json.dumps(schema_json, indent=2, ensure_ascii=False)}\n</script>'


# ---------------------------------------------------------------------------
# WordPress REST API calls
# ---------------------------------------------------------------------------

def get_existing_post(auth: HTTPBasicAuth, wp_url: str, slug: str, post_type: str = "pages") -> dict | None:
    """Check if a page/post with this slug already exists. Returns post data or None."""
    endpoint = f"{wp_url}/wp-json/wp/v2/{post_type}"
    resp = requests.get(endpoint, auth=auth, params={"slug": slug, "status": "any"})
    if resp.status_code == 200:
        posts = resp.json()
        if posts:
            return posts[0]
    return None


def create_or_update_page(
    auth: HTTPBasicAuth,
    wp_url: str,
    payload: dict,
    post_type: str = "pages"
) -> dict:
    """Create a new page/post or update it if the slug already exists.

    Returns: { status: SUCCESS|FAILED, url, post_id, action: created|updated, error }
    """
    endpoint = f"{wp_url}/wp-json/wp/v2/{post_type}"

    # Check for existing post with same slug
    existing = get_existing_post(auth, wp_url, payload.get("slug", ""), post_type)

    if existing:
        # UPDATE (PUT) existing post
        update_endpoint = f"{endpoint}/{existing['id']}"
        resp = requests.put(update_endpoint, auth=auth, json=payload)
        action = "updated"
        post_id = existing["id"]
    else:
        # CREATE (POST) new post
        resp = requests.post(endpoint, auth=auth, json=payload)
        action = "created"
        post_id = None

    if resp.status_code in (200, 201):
        data = resp.json()
        return {
            "status": "SUCCESS",
            "url": data.get("link", ""),
            "post_id": data.get("id"),
            "action": action,
            "error": None
        }
    else:
        return {
            "status": "FAILED",
            "url": None,
            "post_id": post_id,
            "action": action,
            "error": f"HTTP {resp.status_code}: {resp.text[:500]}"
        }


def set_yoast_meta(auth: HTTPBasicAuth, wp_url: str, post_id: int, meta: dict):
    """Set Yoast SEO meta fields via REST API (requires Yoast SEO 14.0+)."""
    endpoint = f"{wp_url}/wp-json/wp/v2/pages/{post_id}"
    yoast_payload = {
        "yoast_head_json": {
            "og_description": meta.get("meta_description", ""),
        },
        "meta": {
            "_yoast_wpseo_metadesc": meta.get("meta_description", ""),
            "_yoast_wpseo_title": meta.get("seo_title", ""),
        }
    }
    requests.put(endpoint, auth=auth, json=yoast_payload)


def set_rank_math_meta(auth: HTTPBasicAuth, wp_url: str, post_id: int, meta: dict):
    """Set Rank Math SEO meta fields via REST API (requires Rank Math 1.0.54+)."""
    endpoint = f"{wp_url}/wp-json/wp/v2/pages/{post_id}"
    rank_math_payload = {
        "meta": {
            "rank_math_description": meta.get("meta_description", ""),
            "rank_math_title": meta.get("seo_title", ""),
            "rank_math_focus_keyword": meta.get("focus_keyword", ""),
        }
    }
    requests.put(endpoint, auth=auth, json=rank_math_payload)


# ---------------------------------------------------------------------------
# Main deployment function
# ---------------------------------------------------------------------------

def deploy_page(page_payload: dict, credentials: dict) -> dict:
    """Full deployment pipeline for a single page.

    page_payload schema:
    {
        "title": "Page Title",
        "slug": "page-slug",
        "content_html": "<article>...</article>",
        "meta_description": "...",
        "seo_title": "...",
        "focus_keyword": "...",
        "schema_json": { "@context": "...", "@type": "..." },
        "internal_links": { "Anchor Text": "https://site.com/slug" },
        "post_type": "pages",          // "pages" or "posts"
        "status": "draft",             // "draft" or "publish"
        "parent_id": 0,                // optional: parent page ID
        "seo_plugin": "rank_math",     // "rank_math", "yoast", or "none"
        "menu_order": 0                // optional: page order
    }
    """
    auth = HTTPBasicAuth(credentials["wp_user"], credentials["wp_app_password"])
    wp_url = credentials["wp_url"]

    # 1. Build content — inject internal links
    content_html = page_payload.get("content_html", "")
    internal_links = page_payload.get("internal_links", {})
    if internal_links:
        content_html = inject_internal_links(content_html, internal_links)

    # 2. Build WP REST payload
    schema_json = page_payload.get("schema_json")
    schema_block = build_schema_block(schema_json) if schema_json else ""

    wp_payload = {
        "title": page_payload["title"],
        "slug": page_payload.get("slug", ""),
        "content": content_html,
        "status": page_payload.get("status", "draft"),
        "parent": page_payload.get("parent_id", 0),
        "menu_order": page_payload.get("menu_order", 0),
        # Custom field for schema (works with ACF, Custom Fields, or theme hooks)
        "meta": {
            "_page_schema_json_ld": json.dumps(schema_json) if schema_json else "",
            "_schema_block_html": schema_block,
        }
    }

    # 3. Deploy via REST API
    post_type = page_payload.get("post_type", "pages")
    result = create_or_update_page(auth, wp_url, wp_payload, post_type)

    if result["status"] == "FAILED":
        return result

    post_id = result["post_id"]

    # 4. Set SEO meta fields
    seo_plugin = page_payload.get("seo_plugin", "rank_math")
    seo_meta = {
        "meta_description": page_payload.get("meta_description", ""),
        "seo_title": page_payload.get("seo_title", page_payload["title"]),
        "focus_keyword": page_payload.get("focus_keyword", ""),
    }

    if seo_plugin == "rank_math" and post_id:
        set_rank_math_meta(auth, wp_url, post_id, seo_meta)
    elif seo_plugin == "yoast" and post_id:
        set_yoast_meta(auth, wp_url, post_id, seo_meta)

    result["meta_set"] = seo_plugin
    result["slug"] = page_payload.get("slug", "")
    return result


# ---------------------------------------------------------------------------
# Batch deployment
# ---------------------------------------------------------------------------

def deploy_batch(batch_payload: dict, credentials: dict) -> list:
    """Deploy multiple pages in order. Respects parent_id ordering.

    batch_payload: { "pages": [ ...page_payload objects... ] }
    Pages are deployed in the order provided — put parent pages first.
    """
    pages = batch_payload.get("pages", [])
    results = []
    slug_to_url = {}  # Build up link map as pages deploy

    for page in pages:
        # Inject already-deployed pages into internal_links
        existing_links = page.get("internal_links", {})
        merged_links = {**slug_to_url, **existing_links}
        page["internal_links"] = merged_links

        result = deploy_page(page, credentials)
        result["title"] = page.get("title", "")
        results.append(result)

        # Add to slug_to_url map for subsequent pages
        if result["status"] == "SUCCESS" and result.get("url"):
            slug_to_url[page["title"]] = result["url"]

    return results


# ---------------------------------------------------------------------------
# CLI interface
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Deploy pages to WordPress 6.9 via REST API"
    )
    parser.add_argument(
        "--payload", type=str, required=True,
        help="Path to JSON file: single page_payload OR batch { pages: [...] }"
    )
    parser.add_argument(
        "--credentials", type=str, required=True,
        help="Path to wp_credentials.json"
    )
    parser.add_argument(
        "--mode", type=str, choices=["single", "batch"], default="single",
        help="Deploy a single page or a batch"
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Optional: save results JSON to this file path"
    )
    args = parser.parse_args()

    try:
        credentials = load_credentials(args.credentials)
    except Exception as e:
        print(json.dumps({"status": "FAILED", "error": f"Credentials error: {e}"}))
        sys.exit(1)

    with open(args.payload, "r", encoding="utf-8") as f:
        payload = json.load(f)

    if args.mode == "batch":
        results = deploy_batch(payload, credentials)
        output = {"results": results, "total": len(results),
                  "success": sum(1 for r in results if r["status"] == "SUCCESS"),
                  "failed": sum(1 for r in results if r["status"] == "FAILED")}
    else:
        output = deploy_page(payload, credentials)

    output_json = json.dumps(output, indent=2, ensure_ascii=False)
    print(output_json)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_json)
        print(f"\nResults saved to {args.output}", file=sys.stderr)
