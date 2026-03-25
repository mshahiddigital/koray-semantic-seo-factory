# Sheets (Online Umrah Taxi)

These CSVs are designed to be imported into Google Sheets/Excel.

## Files
- pages.csv: canonical page inventory (slug, intent, phase, schema, brief path).
- routes.csv: route matrix with placeholders for distance/time/prices.
- queries_full.csv: expanded query universe mapped to target pages.
- entities_eav.csv: entity/attribute/value placeholders to cover across key pages.
- faqs.csv: FAQ backlog mapped to pages.
- internal_links.csv: internal link edges + anchor variants.
- master_sheet.csv: page-centric rollup (queries + links + schema).

## Import
Google Sheets -> File -> Import -> Upload -> select CSV.
