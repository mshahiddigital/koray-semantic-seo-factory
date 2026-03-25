---
name: koray-content-calendar-planner
description: Build a 30/60/90-day content publishing and update calendar that closes semantic gaps, builds topical authority momentum, and sequences pages for maximum internal linking impact. Use for requests like "content calendar", "publishing schedule", "30-day plan", "what to publish next", "update schedule", "content roadmap", or "rapid iteration plan".
---

# Koray Content Calendar Planner

## Workflow

1. Collect inputs: topical map (core/outer), gap list with priorities, existing page inventory, available writing capacity (pages/week).
2. Sequence pages using these rules:
   - Publish hub (core entity) pages first — they receive links from all spokes.
   - Publish highest-P0-gap pages before P1/P2.
   - Batch pages that share a hub so internal links activate together.
   - Space outer section pages to fill momentum gaps between core page groups.
3. Set update triggers for existing pages:
   - Updateness rule: any page older than 90 days with GSC impression growth should be refreshed.
   - Pages that fail HCU audit (score < 80) get scheduled for rewrite before new pages.
4. Output a calendar by week with assigned agents/owners and expected deliverables.

## Update frequency guidelines

- Core / money pages: review every 30 days if high-intent traffic exists.
- Outer / historical nodes: review every 90 days or when a regulation/event changes.
- Pages with "as of [date]" claims: schedule refresh before that date becomes stale (90 days max).

## Output

- **Publishing calendar** (week-by-week): `Week | Page title | Type (new/update) | Priority | Agent | Status`
- **Batching logic** (which pages should go live together for internal linking activation)
- **Update triggers list**: `Page | Last updated | Trigger | Scheduled refresh date`
- **30-day quick wins** (highest-impact pages that can be published first with minimal new research)
