---
name: koray-schema-markup-creator
description: Generate production-ready Schema.org structured data markup for pages based on their EAV triples and content type, then audit existing schema for correctness. Use for requests like "add schema markup", "structured data", "JSON-LD", "FAQPage schema", "HowTo schema", "LocalBusiness schema", "schema audit", or "rich results setup".
---

# Koray Schema Markup Creator

## Workflow

1. Identify the page type and conversion goal (service page, article, FAQ, how-to, local business, product, breadcrumb).
2. Map the page's EAV triples to Schema.org properties — only include properties supported by actual content.
3. Select schema types (use the minimum needed; avoid over-stacking):
   - `WebPage` / `Article` / `BlogPosting` — all content pages
   - `FAQPage` — pages with Q&A sections (3+ distinct questions)
   - `HowTo` — step-by-step instructional pages
   - `LocalBusiness` / `Service` — location/service pages
   - `BreadcrumbList` — navigation structure
   - `Product` — product/pricing pages
   - `Organization` / `Person` — E-E-A-T identity pages
4. Write JSON-LD for each schema type selected.
5. Run a readiness audit: check for missing required properties, unsupported claims, and duplicate schema.

## Schema rules

- Only mark up content that exists on the page — no invented values.
- `FAQPage` requires actual Q&A pairs visible on the page.
- `HowTo` requires numbered steps with real instructions.
- Do not stack `Article` + `FAQPage` on the same page element — nest them correctly.
- `LocalBusiness` must include real address, phone, and hours if they exist.

## Output

- **JSON-LD blocks** (one per schema type, ready to paste into `<head>`)
- **Schema readiness checklist**: `Schema type | Required properties | Present? | Fix`
- **Validation notes** (common Google Rich Results Test failures to check)
- **Implementation instructions** (where to place each block in the CMS/template)

## References (load only if needed)

- `references/eav-modeling-guide.md`
