---
name: koray-hcu-quality-auditor
description: Audit a page/draft for Helpful Content + quality issues using a scored rubric (0–100) covering task completion, E-E-A-T signals, content integrity, conversion UX, internal linking, structured data, and sensitivity for local/religious contexts. Pages scoring below 80 are not ship-ready. Use for requests like "HCU audit", "quality audit", "helpfulness review", "E-E-A-T check", "is this page ready to publish", or "what to fix on this page".
---

# Koray HCU + Quality Auditor

## Always load

- `references/hcu-signals-checklist.md`

## Scoring rule

Score each category 0–100. Total weighted score below 80 = not ship-ready; trigger `koray-holistic-writing-optimizer` before publishing.

## Workflow

1. Identify the target (file path, pasted text, or URL + copied content) and the primary query/task the page must complete.
2. Load `references/hcu-signals-checklist.md` and any project-specific rubric (e.g. `projects/<project>/audit/hcu-quality-audit.md`).
3. Run the audit rubric category-by-category.
4. Score each category and calculate the total.
5. Produce a prioritized fix list (P0 blockers → P1 improvements → P2 polish) with exact rewrite guidance.
6. Provide a final ship checklist.

## Audit rubric

**Helpfulness / task completion (30 points)**

- Answer first — no buried lede
- All constraints covered (price, eligibility, location, time)
- Next steps explicit and actionable

**Experience + trust signals (20 points)**

- Identity clear (who is behind this page)
- Policies present (cancellation, privacy, contact)
- Proof/evidence (reviews, case studies, credentials)
- Support contact accessible

**Content integrity (20 points)**

- No invented numbers or unverified claims
- No overpromises ("guaranteed", "always")
- No duplicate intent pages in the same site section

**Sensitivity (when relevant) (10 points)**

- Local/religious context handled respectfully and accurately
- Special assistance stated honestly without overpromising

**Conversion UX (10 points)**

- Above-the-fold CTA present and intent-matched
- Contact/booking flow frictionless
- Forms match user intent

**Structured data (5 points)**

- Schema types match actual content (`LocalBusiness`, `Service`, `FAQPage`, `BreadcrumbList`)
- No unsupported schema claims

**Internal linking (5 points)**

- No orphan pages
- Hub/spoke alignment present
- Anchors match destination intent/title exactly

## Output

- **Quality score**: `Category | Points earned | Max | Notes`
- **Total score** (0–100) with ship-readiness verdict
- **Executive summary** (3–6 bullets on biggest issues)
- **Issue table**: `Severity | Section | Problem | Why it matters | Fix (specific)`
- **Rewrite suggestions** (highest-impact sections only)
- **Schema + internal linking recommendations**
- **Ship checklist** (pass/fail per criterion)
