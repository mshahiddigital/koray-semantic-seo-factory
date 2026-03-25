---
name: koray-crawl-budget-semantic-optimizer
description: Optimize a site's Cost of Retrieval — the technical and semantic factors that determine how efficiently Google can crawl, parse, and resolve entities on your pages. Covers semantic HTML structure, internal link depth, crawl waste reduction, and entity disambiguation. Use for requests like "crawl budget", "cost of retrieval", "crawl optimization", "entity resolution", "HTML semantics", "crawl efficiency", "reduce crawl waste", or "technical semantic SEO".
---

# Koray Crawl Budget + Semantic Optimizer

## Cost of Retrieval components

**1. Semantic HTML quality**

- Heading hierarchy: H1 = central entity + macro context, H2 = core attributes, H3 = sub-attributes
- One H1 per page, no skipped heading levels
- `<article>`, `<main>`, `<nav>`, `<footer>` landmark elements used correctly
- No content in `<div>` soup when semantic elements apply

**2. Entity resolution clarity**

- Central entity named explicitly in H1 and first paragraph
- Entity disambiguated by source context (e.g., "Makkah Taxi Service in Saudi Arabia" not just "taxi service")
- `name`, `description`, `url` properties present in `Organization`/`LocalBusiness` schema

**3. Internal link depth**

- No page more than 3 clicks from the homepage
- Hub pages linked from homepage or top-level navigation
- Spoke pages linked from their hub — not only from footer or sidebar

**4. Crawl waste elimination**

- No duplicate content (two URLs resolving to same content without canonical)
- No thin pages below 300 words without a clear intent to serve
- URL structure: `/central-entity/primary-attribute/` — no ID parameters in important URLs
- Canonical tags on all paginated, filtered, or near-duplicate variants

**5. Page speed and rendering**

- Core Web Vitals: LCP < 2.5s, CLS < 0.1, INP < 200ms
- Avoid JavaScript-only content rendering for primary entity content
- Critical text content in HTML, not loaded by JS after page paint

## Workflow

1. Identify target pages/site and available data (crawl export, GSC coverage report, PageSpeed data).
2. Audit each component using evidence (not assumptions).
3. Prioritize: P0 (pages blocked or not indexed) → P1 (entity resolution failures) → P2 (depth/speed).
4. Produce a technical fix plan with specific implementation instructions.

## Output

- **Cost of Retrieval score** (0–100, weighted by component)
- **Issue table**: `Component | Issue | Affected pages | Fix | Priority`
- **HTML structure recommendations** (heading map per template)
- **URL structure recommendations**
- **Schema entity resolution improvements**

## References (load only if needed)

- `references/topical-authority-formula.md`
- `koray-patent-researcher` (for retrieval-cost patent insights)
