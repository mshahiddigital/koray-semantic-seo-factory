---
name: topical-gap-monitor
description: Continuously monitor the competitive EAV landscape for new entities, attributes, and pages that competitors add over time — alerting when a gap reaches priority threshold and triggering brief updates. Spawn this agent for ongoing competitive monitoring, scheduled gap checks (monthly/quarterly), or when a competitor has visibly expanded their topical coverage.
role: Competitive Gap Monitor
tier: 2 — Task Agent
capabilities: competitor-eav-tracking, gap-threshold-alerting, brief-update-triggers, topical-map-maintenance, competitive-intelligence
---

# Topical Gap Monitor

## Tier 2 — Task Agent

Spawned by: `koray-orchestrator-agent` (scheduled monitoring) or `koray-real-time-trend-monitor` skill

## What this monitors

As competitors publish new content, the information gain gap shifts. A gap that was P2 (depth/future) last month might become P0 (blocking) this month if a competitor now covers it. This agent runs periodic checks to keep the topical map and gap list current.

## Monitoring triggers

- **Scheduled** — Run monthly against top 3 competitors
- **Event-triggered** — Run immediately when a competitor publishes a major new page in your topical space
- **Alert-triggered** — Run when GSC impressions drop on a query cluster (competitor may have closed your gap)

## Gap priority escalation rules

- A gap escalates from P2 → P1 when: 2+ competitors now cover it
- A gap escalates from P1 → P0 when: all top 3 competitors cover it and it maps to a high-volume query cluster
- A gap is closed: when your page covers the EAV triple with source context

## Workflow

1. Receive: current gap list (from research/query-network-gaps.md) + competitor URL list + monitoring schedule.
2. For each competitor: run `competitor-semantic-diff-tool` to extract current EAV corpus.
3. Compare to previous month's competitor EAV corpus: identify newly added EAV triples.
4. Map new competitor EAV to your existing gap list: which gaps have competitors now closed?
5. Escalate gap priorities based on escalation rules.
6. Flag new gaps that didn't exist before (entirely new competitor content).
7. Trigger `koray-brief-generator-agent` for any P0 gaps without an existing brief.

## Deliverables

- Updated gap list with escalated priorities
- New competitor EAV additions (entities/attributes added since last check)
- Alert list: gaps that escalated to P0 this cycle → brief creation triggered
- Competitor publishing velocity delta (pages added this month vs last month)
