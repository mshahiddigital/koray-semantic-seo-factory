---
name: koray-eav-triple-semantic-brief-generator
description: Generate a semantic SEO content brief using Koray-style EAV triples (Entity–Attribute–Value) + source context, lexical relations, paragraph functions, query-intent templates, and internal-linking suggestions. Use for requests like "semantic content brief", "EAV table", "entity attribute value", "Koray brief for [topic/page]", "create a brief", or "brief for [page title]".
---

# Koray EAV + Semantic Brief Generator

## Always load

- `references/eav-modeling-guide.md`

## Workflow

1. Collect inputs (topic/page, target country/language, audience, conversion goal, constraints, competitor URLs or notes if available).
2. Define the **central entity** and 5–15 supporting entities (products, places, organizations, processes, policies).
3. Build the **EAV table** with evidence (minimum 10 triples per page):
   - Columns: `Entity | Attribute | Value | Source Context`
   - Use explicit source context (quote/snippet, page section, or provided data)
   - Label unknowns as `Unknown` and list questions to confirm
   - Flag any invented values immediately — stop and ask for data
4. Produce the **lexical relations list**:
   - Synonyms/near-synonyms, hypernyms/hyponyms, attributes, parts, related processes, constraints, comparisons
5. Draft a **heading + paragraph function map**:
   - For each H2/H3: state the paragraph function (definition, steps, eligibility, pricing policy, comparison, FAQ, etc.) and the immediate answer to lead with
6. Add **query-intent templates**:
   - Map each section to intents (know / do / buy / local / troubleshooting) and example queries
7. Add an **internal linking plan**:
   - Recommend 5–15 internal targets (existing pages if provided; otherwise propose future nodes) with anchor text suggestions and placement notes

## Quality bar

- Minimum 10 EAV triples per brief.
- Every EAV row needs source context — `Unknown` is acceptable, invented values are not.
- Headings must complete tasks (answer first, elaborate second).
- Internal link anchors must match destination page title exactly.

## Output (always include)

- **EAV Table** (`Entity | Attribute | Value | Source Context`)
- **Lexical Relations** (bulleted by entity/section)
- **Heading + Paragraph Functions** (table: `Heading | Function | Lead answer`)
- **Query–Intent Templates** (table: `Section | Intent | Example queries`)
- **Internal Linking Plan** (`Source section | Target page | Anchor | Rationale`)
