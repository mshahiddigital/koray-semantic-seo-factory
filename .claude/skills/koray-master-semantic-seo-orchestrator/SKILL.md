---
name: koray-master-semantic-seo-orchestrator
description: Run the end-to-end Koray semantic SEO workflow for a project using parallel agent execution (topical map + query research simultaneously → internal linking + batch briefs simultaneously → writing + Python scripts simultaneously → HCU audits). Use when asked to "run the full Koray workflow", "build topical authority", "start an SEO project", or "deliver the complete plan + artifacts for a niche/site".
---

# Koray Master Semantic SEO Orchestrator

## Workflow

1. Collect inputs: niche/site, country/language, business model, seed topics, target pages (if any), competitor URLs/content, and any GSC/analytics exports the user can provide.
2. Ask for any missing critical inputs before starting — especially: pricing/policies, GSC access, competitor URLs.
3. Create `projects/<project-slug>/` with subfolders: `research/`, `briefs/`, `content/`, `network/`, `audit/`, `sheets/`.

**Phase 1 — Run simultaneously (spawn parallel agents):**

- `koray-mapper-agent` → builds topical map + coverage score
- `koray-researcher-agent` → builds query network + gap list

**Phase 2 — Run simultaneously after Phase 1 (spawn parallel agents):**

- `koray-network-planner-agent` → designs internal linking plan from topical map
- `koray-brief-generator-agent` × N → generates one brief per planned page (batches of 5–10)

**Phase 3 — Run simultaneously after Phase 2 (spawn parallel agents):**

- `koray-writer-agent` in batches of 5–10 → writes and optimizes pages from briefs
- `koray-python-engineer-agent` → runs scripts, compiles research sheet CSV

**Phase 4 — After Phase 3 (run auditor):**

- `koray-auditor-agent` × N → audits all written pages; pages scoring < 80 go back to writer

4. Verify all deliverables exist under `projects/<slug>/` after each phase before proceeding.
5. Output the 30-day action plan.

## Output (minimum)

- `projects/<slug>/research/topical-map.md`
- `projects/<slug>/research/query-network-gaps.(md|csv)`
- `projects/<slug>/network/internal-linking-plan.md`
- `projects/<slug>/briefs/` (one brief per planned page)
- `projects/<slug>/content/` (optimized drafts)
- `projects/<slug>/audit/` (audits for all pages)
- `projects/<slug>/research/research_sheet.csv`
- `projects/<slug>/sheets/master_sheet.csv`
- 30-day action plan (next pages to publish, update triggers, gap closure priorities)

## Guardrails

- Ask targeted questions instead of guessing (pricing, policies, operational constraints).
- Avoid creating duplicate pages for minor keyword variants.
- Never proceed to Phase 2 without a completed topical map and query network.
- Never mark a page as complete if its HCU score is below 80.
