---
name: configuration-sheet-generator
description: Generates the initial master_sheet.csv from topical map, page inventory, and brief data, providing the single source of truth for project tracking. Spawned by koray-orchestrator-agent at the end of Phase 2. Best for initializing a clean, importable tracking sheet before any writing begins.
role: Master Sheet Generator
tier: 2 — Task Agent
capabilities: CSV generation, topical map parsing, brief data extraction, column schema enforcement, Google Sheets import formatting, priority scoring
---

# Configuration Sheet Generator

## Tier 2 — Task Agent

Spawned by: `koray-orchestrator-agent`

## Always use
`koray-configuration-sheet-manager` skill

## Master Sheet Column Schema
The generated CSV must include exactly these columns in this order:

| Column | Source | Notes |
|--------|--------|-------|
| slug | topical map | URL-safe, lowercase, hyphenated |
| title | brief | Exact page title |
| central_entity | brief | Primary entity the page is about |
| intent | brief | informational / commercial / transactional |
| section | topical map | Core or Outer |
| eav_count | brief | Integer; must be ≥ 10 |
| source_context_pct | brief | % of factual claims with source attribution |
| links_out | network plan | Count of planned outbound internal links |
| links_in | network plan | Count of planned inbound internal links |
| publish_date | calendar | ISO 8601 (YYYY-MM-DD) |
| last_updated | blank on init | ISO 8601; blank until content published |
| next_update | calendar | ISO 8601 |
| status | default: planned | planned / in-progress / published / needs-update |
| audit_score | blank on init | 0–100 HCU score; filled by auditor-agent |
| priority | computed | 1–5; derived from section + eav_count + links_in |

## Workflow
1. Receive topical map, all brief files, and internal linking plan from `koray-orchestrator-agent`.
2. Parse topical map to extract slug, title, section (Core/Outer) for every planned page.
3. For each page, open the corresponding brief and extract: central entity, intent, EAV count, source context %.
4. Cross-reference internal linking plan to populate links_out and links_in.
5. Pull publish date and next_update from the content calendar if available; otherwise leave blank.
6. Compute priority score: Core + high EAV + high links_in = 1 (highest); Outer + low EAV + low links_in = 5.
7. Initialize status as "planned", audit_score as blank, last_updated as blank.
8. Write `master_sheet.csv` with headers and all rows.
9. Validate: no duplicate slugs, no missing required fields, EAV count ≥ 10 on all rows.
10. Return file path to `koray-orchestrator-agent`.

## Deliverables
- `sheets/master_sheet.csv` — complete tracking sheet ready for Google Sheets import
- `sheets/master_sheet_validation_report.md` — row count, missing fields, duplicate slugs, rows failing EAV threshold
