---
name: koray-topical-authority-scorer
description: Calculate a numeric Topical Authority score for a site/niche using Koray's formula (Coverage × Historical Data × Cost of Retrieval + Momentum + Depth + Vastness + Updateness), identify the weakest components, and produce a prioritized improvement plan. Use for requests like "topical authority score", "TA score", "calculate authority", "coverage score", "how strong is our topical authority", or "information gain score".
---

# Koray Topical Authority Scorer

## Formula

```
Topical Authority = (Coverage × Historical Data × Cost of Retrieval) + (Momentum + Depth + Vastness + Updateness)
```

Target threshold: **85+** = unbreakable authority in niche (outperforms Wikipedia-level competitors).

## Component definitions and scoring inputs

**Coverage (30% weight, score 0–100)**

- EAV completeness vs top 3 competitors
- Input: your EAV count / competitor EAV count × lexical overlap × query coverage %

**Historical Data (20% weight, score 0–100)**

- Site age, backlink history, content update log, original publication dates
- Input: domain age in years, # of historical nodes (timelines, evolutions, regulations), # of quality backlinks

**Cost of Retrieval (20% weight, score 0–100)**

- Semantic HTML quality, structured data coverage, crawl efficiency, entity resolution clarity
- Input: schema types implemented, page speed score, HTML heading hierarchy quality, internal link depth

**Momentum (10% weight, score 0–100)**

- GSC click/impression growth trend over 90 days
- Input: GSC data or proxy signals (content publish cadence, engagement)

**Depth (10% weight, score 0–100)**

- Average paragraph depth: EAV attribute detail, source context density, paragraph function completeness
- Input: avg EAV triples per page, % of sections with source context

**Vastness (5% weight, score 0–100)**

- Breadth of related entities and bridge topics covered in outer sections
- Input: # of outer section nodes, # of unique entities covered across the site

**Updateness (5% weight, score 0–100)**

- Freshness signals: "as of [date]" usage, update frequency, new data additions
- Input: # of pages updated in last 90 days, % of pages with explicit date stamps

## Workflow

1. Collect available inputs (topical map, EAV data, GSC export, domain info, competitor baseline).
2. Score each component 0–100 based on evidence; estimate missing inputs with explicit assumptions.
3. Calculate the weighted total score.
4. Identify the two lowest-scoring components — those are the highest-priority improvements.
5. Produce a component improvement plan with specific actions.

## Output

- **Score breakdown table**: `Component | Weight | Your score | Max | Weighted score`
- **Total TA score** (0–100)
- **Gap vs threshold** (how far from 85)
- **Improvement plan**: `Component | Current gap | Action | Expected score lift | Priority`

## References (load only if needed)

- `references/topical-authority-formula.md`
