---
name: wp-deploy
description: Deploy one or more pages to an existing WordPress 6.9+ site via the REST API — validating schema first, injecting internal links, setting SEO meta fields (Rank Math or Yoast), and logging results. Use for requests like "deploy to WordPress", "publish this page", "push content to WP", "deploy batch to WordPress", or "WordPress REST API deploy".
---

# WordPress Deploy Skill

## Purpose

Push Koray-audited content (HCU ≥ 80) to a live WordPress 6.9+ installation via the REST API. Handles single pages and batches. Always validates schema before deploy.

## Pre-conditions (must be met before deploy)

- [ ] HCU audit score ≥ 80 for every page
- [ ] Schema validated via `validate-schema` skill (no critical errors)
- [ ] `wp_credentials.json` exists with `wp_url`, `wp_user`, `wp_app_password`
- [ ] Page payload JSON file is ready in `projects/<slug>/content/`

## Credential setup (one-time)

Create `projects/<slug>/wp_credentials.json`:
```json
{
  "wp_url": "https://yoursite.com",
  "wp_user": "admin",
  "wp_app_password": "xxxx xxxx xxxx xxxx xxxx xxxx"
}
```

Generate Application Password in WP Admin → Users → Profile → Application Passwords.
**Never store the admin password — Application Passwords only.**

## Page payload format

```json
{
  "title": "Page Title Here",
  "slug": "page-slug",
  "content_html": "<article>...</article>",
  "meta_description": "150-char description",
  "seo_title": "Title for SERP | Site Name",
  "focus_keyword": "primary keyword",
  "schema_json": { "@context": "https://schema.org", "@type": "..." },
  "internal_links": { "Anchor Text": "https://site.com/slug" },
  "post_type": "pages",
  "status": "draft",
  "parent_id": 0,
  "seo_plugin": "rank_math",
  "menu_order": 0
}
```

## Deployment process

1. Load `wp_credentials.json` for the target site
2. Run `validate-schema` on each page's `schema_json` — abort if critical errors
3. Run `python python-backend/wp_deployer.py --payload <file> --credentials <creds> --mode single`
4. For batches: `--mode batch` — parent pages deploy first (ordered by `parent_id`)
5. Parse output: `SUCCESS` → log URL; `FAILED` → read error, fix payload, retry once
6. Save results to `projects/<slug>/sheets/deployed_pages.csv`
7. Trigger `browser-qa-agent` on all deployed URLs

## Batch payload format

```json
{
  "pages": [
    { "title": "Hub Page", "slug": "hub", "parent_id": 0, "status": "draft", ... },
    { "title": "Spoke Page", "slug": "spoke", "parent_id": 0, "status": "draft", ... }
  ]
}
```

## Status options

| Status | When to use |
| ------ | ----------- |
| `"draft"` | Default — always deploy as draft first, publish after QA |
| `"publish"` | Only after `browser-qa-agent` returns score ≥ 80 |

## CLI reference

```bash
# Single page
python python-backend/wp_deployer.py \
  --payload projects/slug/content/page.json \
  --credentials projects/slug/wp_credentials.json \
  --mode single

# Batch (full site)
python python-backend/wp_deployer.py \
  --payload projects/slug/content/batch_payload.json \
  --credentials projects/slug/wp_credentials.json \
  --mode batch \
  --output projects/slug/sheets/deployed_pages.json
```

## Supported SEO plugins

- `rank_math` — sets `rank_math_description`, `rank_math_title`, `rank_math_focus_keyword`
- `yoast` — sets `_yoast_wpseo_metadesc`, `_yoast_wpseo_title`
- `none` — skips SEO meta (use for sites with custom implementations)
