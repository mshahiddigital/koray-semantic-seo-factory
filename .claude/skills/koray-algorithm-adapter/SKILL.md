---
name: koray-algorithm-adapter
description: Analyze an SEO traffic/visibility drop or suspected Google update impact and adapt the topical map, content, and internal linking plan accordingly. Use for requests like "core update impact", "algorithm change", "traffic drop", "rankings fell", "HCU hit", "helpful content update", "March core update", or "how to adapt our topical authority strategy".
---

# Koray Algorithm Adapter

## Always load

- `references/hcu-signals-checklist.md`

## Workflow

1. Define the incident window (exact dates), affected pages/queries, and available data sources (GSC, analytics, rank tracker, crawl export).
2. Form hypotheses only from evidence — match symptoms to likely causes:
   - Traffic drop across site → likely topical authority / HCU signal
   - Traffic drop on specific pages → likely intent mismatch or content integrity
   - Ranking drops on commercial pages → likely E-E-A-T or conversion UX
   - Rankings dropped then partially recovered → likely freshness or duplicate intent
   - Indexed pages reduced → likely crawl budget / thin content
3. Re-audit the most affected pages using `koray-hcu-quality-auditor` (score each; prioritize pages below 70).
4. Apply `koray-holistic-writing-optimizer` to any page scoring below 80.
5. Re-check the topical map for structural issues:
   - Missing nodes competitors have
   - Core vs outer imbalance (too many thin outer pages, no strong core hub)
   - Cannibalization: two pages targeting same intent
   - Orphan pages with no inbound internal links
6. Check `koray-e-e-a-t-entity-builder` signals if the drop correlates with a YMYL or authority-related update.
7. Produce an adaptation plan with phased execution.
8. If the user requests external confirmation, use web research to summarize what the update targeted — but keep all actions grounded in the site's actual issues.

## Output

- **Diagnosis summary** (what likely changed, evidence, confidence level)
- **Page-level fix plan**: `Page | HCU score | Issue | Fix | Priority`
- **Map/network adjustments** (nodes to add/merge/remove + linking changes needed)
- **E-E-A-T gaps** (if applicable)
- **30-day execution plan** (P0 this week → P1 next 2 weeks → P2 month 2)

## References (load if needed)

- `references/topical-authority-formula.md`
