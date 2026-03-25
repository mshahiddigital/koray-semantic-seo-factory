---
name: koray-semantic-content-network-planner
description: Design a semantic content network + internal linking plan (hub/spoke, core vs outer support nodes, anchor mapping, and contextual link placements) aligned to a topical map and query network. Use for requests like "internal linking plan", "content network", "hub and spoke", "site structure", or "topic cluster linking".
---

# Koray Semantic Content Network Planner

## Workflow
1. Inputs: topical map (core/outer), planned pages, and any existing URLs/slugs.
2. Define hubs (core entities) and spokes (supporting attributes, comparisons, FAQs, how-tos).
3. Specify link rules:
   - Link direction (hub ↔ spoke, sibling spokes, outer → core where relevant)
   - Anchor strategy (match destination title/intent; avoid generic anchors)
   - Placement strategy (place links in the most relevant section; avoid footer-only linking)
4. Produce the internal linking plan and a short set of implementation guardrails.

## Output
- `internal-linking-plan.md` with:
  - **Link table**: `Source page | Target page | Anchor | Placement | Rationale | Priority`
  - **Hub/spoke map** (bullets)
  - **Guardrails** (no orphan pages, avoid overlinking, one intent per page)
