---
name: koray-topical-map-architect
description: Build a Koray-style topical map (core vs outer sections) with central entity definition, source context, query clusters, lexical relations, historical nodes, coverage scoring against the Topical Authority formula, and a prioritized gap list. Use for requests like "topical map", "topic architecture", "core vs outer", "semantic hierarchy for [topic]", "build my topical map", or "what pages do I need for [niche]".
---

# Koray Topical Map Architect

## Always load

- `references/topical-authority-formula.md`
- `references/core-outer-examples.md`

## Workflow

1. Collect inputs: niche/site, country/language, business model, seed topics, and 3–10 key competitors (URLs or notes).
2. Define the **central entity** and the **single macro context** for the entire map (1–2 sentences).
3. Build Core vs Outer sections:
   - **Core**: money-making attributes, direct commercial intents, pages that drive conversions
   - **Outer**: supporting/historical/contextual nodes that strengthen topical depth (timelines, regulations, comparisons, bridge topics)
4. Create query clusters (by intent + proximity) and map each cluster to a page/node.
5. Add lexical relations and key entities per node (minimum viable semantic coverage per page).
6. Add historical nodes: timelines, evolution, regulations, landmark events — these are Outer section staples.
7. Score coverage vs competitors using the Topical Authority formula components:
   - Coverage % = (Your page/EAV count / Competitor count) × Lexical Overlap × Query Coverage
   - Note Historical Data gaps (nodes competitors have that establish longer history)
8. List missing nodes with priority and component impact (Coverage / Historical / Depth).

## Outputs (always include)

- **Central Entity + Source Context** (1–2 sentences)
- **Core Section** (hierarchical bullets with page titles and target intents)
- **Outer Section** (hierarchical bullets with page titles and support roles)
- **Query Clusters** (table: `Cluster | Intent | Suggested page | Notes`)
- **Coverage gaps** (table: `Missing node | TA component affected | Priority`)
- **Coverage score estimate** vs top 3 competitors (0–100)

## References (load if needed for examples)

- `references/query-network-best-practices.md`
- `references/eav-modeling-guide.md`
