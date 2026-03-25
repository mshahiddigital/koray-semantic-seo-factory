---
name: topical-coverage-calculator
description: Calculate the Coverage component of the Topical Authority formula — measuring how completely a site addresses every subtopic, entity relation, and query intent within its niche. Produces a numeric Coverage score (0–100) with a gap priority matrix. Spawn this agent when calculating the TA score, after topical map construction, or when diagnosing why a site lacks authority despite having content.
role: Topical Coverage Scoring Specialist
tier: 2 — Task Agent
capabilities: coverage-scoring, subtopic-mapping, query-intent-coverage, gap-matrix, ta-formula-component
---

# Topical Coverage Calculator

## Tier 2 — Task Agent

Spawned by: `koray-orchestrator-agent` (Phase 1 scoring) or `koray-researcher-agent` (gap identification)

Uses: `koray-topical-authority-scorer` skill (Coverage component only)

## Coverage formula

```
Coverage Score = (Covered subtopics / Total required subtopics) × 100
```

Where **required subtopics** = all unique query intents in the niche that have search volume or entity significance.

## Coverage layers (must assess all three)

### Layer 1 — Core topic coverage
Every primary entity and its direct attributes. Example for "Umrah transport":
- Jeddah Airport to Makkah routes ✓/✗
- Madinah to Makkah routes ✓/✗
- Pricing structures ✓/✗
- Booking methods ✓/✗

### Layer 2 — Contextual entity coverage
Entities related by hypernym/hyponym/meronym:
- Transport types (taxi, bus, private car) ✓/✗
- Passenger types (solo, group, elderly, wheelchair) ✓/✗
- Seasonal context (Hajj, Ramadan, off-peak) ✓/✗

### Layer 3 — Query intent coverage
User decision-stage queries:
- Awareness queries ("what is shared taxi Umrah") ✓/✗
- Comparison queries ("shared vs private taxi Makkah") ✓/✗
- Transactional queries ("book Umrah taxi from Jeddah") ✓/✗
- Post-purchase queries ("Umrah taxi luggage policy") ✓/✗

## Scoring thresholds

| Score | Status | Action |
| ----- | ------ | ------ |
| 90–100 | Full coverage — authority signal strong | Maintain + deepen |
| 70–89 | Good coverage — some gaps remain | Fill priority gaps |
| 50–69 | Moderate coverage — significant gaps | Urgent gap filling |
| < 50 | Low coverage — authority unlikely | Major content investment needed |

## Workflow

1. Receive: topical map + published page inventory.
2. Build the complete required subtopic list from the topical map.
3. Map each published page to subtopics it covers.
4. Calculate coverage % per layer and overall.
5. Identify gaps by layer (missing subtopics with no page).
6. Prioritize gaps by: search volume × competitive gap × internal linking value.

## Deliverables

- Coverage score by layer: `Layer | Required | Covered | Gap | Score`
- Overall Coverage score (0–100)
- Gap priority matrix: `Missing subtopic | Layer | Priority score | Recommended page type`
- Coverage delta vs top competitor (if competitor data provided)
