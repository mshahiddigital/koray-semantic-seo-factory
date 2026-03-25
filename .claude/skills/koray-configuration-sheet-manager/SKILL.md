---
name: koray-configuration-sheet-manager
description: Generate or audit Koray-style Content Configuration Sheets — structured CSV/spreadsheet files that track pages, entities, EAV counts, internal links, update schedules, and semantic iteration status. Use for requests like "configuration sheet", "content tracking sheet", "generate the config CSV", "audit config sheet", "content management sheet", or "semantic iteration tracker".
---

# Koray Configuration Sheet Manager

## What a Configuration Sheet is

A master tracking file for all pages in a project. It connects the topical map to production: what page exists, what entities it covers, what EAV count it has, when it was last updated, and what needs to happen next.

## Workflow — Generate mode

1. Collect inputs: topical map, list of planned/published URLs, any existing briefs.
2. Build the master sheet with these columns (minimum):
   - `Page slug` — URL path
   - `Page title` — exact H1
   - `Central entity` — the one macro entity for the page
   - `Intent` — know / do / buy / local / troubleshooting
   - `Section` — Core or Outer
   - `EAV count` — number of EAV triples in the brief/page
   - `Source context coverage` — % of EAV triples with verified source context
   - `Internal links out` — count of outbound internal links
   - `Internal links in` — count of inbound internal links from other pages
   - `Publish date` — ISO date or blank if not yet published
   - `Last updated` — ISO date
   - `Next update` — recommended next review date
   - `Status` — Draft / In review / Live / Needs refresh
   - `Audit score` — HCU score 0–100 (blank until audited)
   - `Priority` — P0 / P1 / P2
3. Output as CSV and provide Google Sheets import instructions.

## Workflow — Audit mode

1. Load existing configuration sheet.
2. Check for: orphan pages (zero inbound links), pages with EAV < 10, missing source context, overdue update dates, status inconsistencies.
3. Output an issue list with recommended fixes.

## Output

- `projects/<slug>/sheets/master_sheet.csv` (Google Sheets import-ready)
- Issue list (audit mode): `Page | Issue | Recommended fix | Priority`
- Import instructions (which columns to freeze, filter, and sort)
