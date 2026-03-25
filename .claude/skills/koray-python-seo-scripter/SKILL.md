---
name: koray-python-seo-scripter
description: Run and adapt the repo’s SEO Python utilities in `python-backend/` (query clustering, semantic gap reports, EAV extraction, topicality/coverage scoring, SERP scraping, and research sheet compilation). Use for requests like "run the script", "cluster these queries", "generate a gap report", or "compile the research_sheet.csv".
---

# Koray Python SEO Scripter

## Workflow
1. Choose the right script from `python-backend/` based on the deliverable.
2. Confirm inputs/paths (CSV columns, text file encoding, expected output paths).
3. Run the script and capture stdout + output files.
4. If a dependency is missing, stop and ask before installing anything.
5. Summarize results and point to the generated file paths.

## Common commands
- Compile a research sheet:
  - `python python-backend/research_compiler.py --input_json workflow_data.json --output_csv projects/<slug>/research/research_sheet.csv`
- Cluster queries:
  - `python python-backend/query_clusterer.py --queries queries.csv --num_clusters 5 --output_csv projects/<slug>/research/query_clusters.csv`
- Generate a gap report:
  - `python python-backend/gap_report_pipeline.py --queries queries.csv --content my_page.txt --competitors comp1.txt,comp2.txt --output_csv projects/<slug>/research/gap_report.csv`

## Available scripts (repo)
- `python-backend/research_compiler.py`: JSON → CSV research sheet
- `python-backend/query_clusterer.py`: query clustering (CSV or comma-separated)
- `python-backend/gap_report_pipeline.py`: cluster + extract + compare (gap report)
- `python-backend/eav_triple_generator.py`: seed entity → EAV triples (may require extra deps)
- Other utilities: see `python-backend/`

## Output
- Generated file(s) under `projects/<slug>/...`
- A short run log (command used + where outputs were written)
