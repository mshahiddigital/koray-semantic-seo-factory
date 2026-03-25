---
name: koray-query-network-gap-researcher
description: Build a query network and identify semantic/content gaps using Koray-style clustering, intent mapping, and competitor/entity comparison. Use for requests like "query network", "keyword clustering", "semantic gaps", "missing topics", or "turn this GSC export into clusters".
---

# Koray Query Network + Gap Researcher

## Workflow
1. Collect query inputs (preferred order):
   - GSC export CSV (query + clicks/impressions), or
   - a seed keyword list, or
   - competitor headings/FAQs converted into candidate queries.
2. Normalize queries (dedupe, unify casing, remove obvious noise).
3. Cluster into a query network:
   - Prefer `koray-python-seo-scripter` with `python-backend/query_clusterer.py` when runnable.
   - Otherwise cluster manually by intent + lexical similarity and document the heuristic.
4. Identify gaps:
   - Compare your page/entity coverage vs competitors and/or the topical map.
   - Output gaps per cluster with suggested sections/pages to close each gap.
5. Prioritize:
   - P0 = blockers for task completion / conversion
   - P1 = high-intent missing sections
   - P2 = depth / information gain additions

## Output (choose one)
- `query-network-gaps.md` (tables + explanations), or
- `query-network-gaps.csv` (one row per gap)

### Suggested fields
`Cluster | Intent | Gap | Evidence (competitor/source) | Recommended fix (section/page) | Priority`

## References (load only if needed)
- `references/query-network-best-practices.md`
