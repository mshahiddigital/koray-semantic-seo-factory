---
name: koray-dashboard-generator
description: Design an SEO reporting dashboard (Google Sheets/Looker Studio spec) that tracks topical authority execution: pages shipped, query clusters covered, internal links implemented, and quality/audit status. Use for requests like "SEO dashboard", "reporting sheet", "progress tracker", or "operational KPI dashboard".
---

# Koray Dashboard Generator

## Workflow
1. Confirm the audience (founder, SEO lead, writer team) and reporting cadence (weekly/monthly).
2. Confirm available data sources (GSC export, analytics, rank tracker, crawl export, internal project files).
3. Define the dashboard model as tabs:
   - **Pages**: status, target intent, publish date, last updated, primary query cluster, audit score.
   - **Query clusters**: cluster, intent, covered page, impressions/clicks (if available), gap status.
   - **Internal links**: source, target, anchor, implemented (Y/N), date.
   - **Audits**: page, issues count by severity, last audit date, ship readiness.
   - **Roadmap**: next pages to create/refresh by priority.
4. Define KPI cards (choose 6–12): pages shipped, clusters covered, P0 issues open, orphan pages, internal links implemented, audit pass rate.
5. Provide chart suggestions (only if data exists): trend lines, bar charts by intent, coverage %.

## Output
- **Sheet schema** (tabs + column names)
- **KPI definitions** (formula-ready)
- **Dashboard layout notes**
- **Import instructions** (how to paste CSV exports into the tabs)
