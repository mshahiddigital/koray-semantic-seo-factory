---
name: koray-programmatic-page-generator
description: Plan and generate programmatic SEO pages from a topical map + EAV data (templates, data schema, and QA rules) for scaling to large page counts. Use for requests like "programmatic SEO", "scale to 1000 pages", "bulk page generation", or "template + CSV for CMS import".
---

# Koray Programmatic Page Generator

## Workflow
1. Confirm the page type to scale (routes, locations, products, FAQs, comparisons) and the conversion goal.
2. Define the data model:
   - Required entities/attributes per page (EAV fields)
   - Optional enrichments (FAQs, comparisons, policies)
3. Design templates:
   - H1/H2/H3 structure
   - Paragraph functions (answer-first)
   - Slots for evidence/policies (avoid invented claims)
4. Define QA guardrails:
   - Prevent near-duplicate pages (unique value requirement)
   - No hallucinated numbers/policies
   - Internal linking rules
   - Minimum semantic coverage per template
5. Produce an import-ready dataset (CSV/JSON spec) and example rows.

## Output
- **Template spec** (Markdown)
- **Data schema** (table: `Field | Type | Required | Notes`)
- **QA checklist**
- **Example CSV rows** (3–10)
