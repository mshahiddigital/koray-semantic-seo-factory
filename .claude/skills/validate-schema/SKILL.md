---
name: validate-schema
description: Validate JSON-LD Schema.org markup for a page against required properties, completeness, and rich result eligibility before deployment. Blocks deployment if critical errors are found. Use for requests like "validate schema", "check schema markup", "is this JSON-LD valid", "schema ready to deploy", or "schema audit".
---

# Validate Schema Skill

## Purpose

Run local Schema.org validation on JSON-LD markup before it is deployed to any website. This is a **required gate** before `wp-deploy-agent` or `new-site-builder` can push content live.

## How to invoke

Provide one of:
- A JSON-LD schema object inline
- A file path to a `.json` schema file
- A page from `projects/<slug>/audit/` (schema block will be extracted)

## Validation process

1. **Run** `python python-backend/schema_validator.py --schema_json '<json>'` (or `--schema_file <path>`)
2. **Interpret results**:
   - `valid: true` + `score: 100` → PASS, cleared for deployment
   - `valid: true` + warnings present → PASS WITH WARNINGS — report warnings, proceed with deploy
   - `valid: false` + errors present → FAIL — do not deploy; provide fix list
3. **Output** a human-readable validation report

## What is validated

| Check | Severity | Blocks deploy? |
| ----- | -------- | -------------- |
| `@context` contains "schema.org" | Critical | Yes |
| `@type` is present and recognized | Critical | Yes |
| Required properties per type | Critical | Yes |
| Recommended properties | Medium | No (warning only) |
| FAQPage: all questions have answers | Critical | Yes |
| HowTo: all steps have text | Critical | Yes |
| BreadcrumbList: items have position + name | Critical | Yes |
| Article: datePublished is ISO 8601 | Medium | No (warning) |
| Nested objects have correct `@type` | High | Yes |

## Types supported

`LocalBusiness`, `MedicalClinic`, `FAQPage`, `HowTo`, `Article`, `BlogPosting`, `Product`, `Organization`, `BreadcrumbList`, `Service`, `Person`, `WebPage`, `WebSite`, `Event`, `Recipe`, `Review`

## Output format

```
SCHEMA VALIDATION REPORT
========================
Types found: FAQPage, BreadcrumbList
Overall: PASS (score: 100/100)

FAQPage — PASS
  ✓ @context: https://schema.org
  ✓ mainEntity: 6 questions found
  ✓ All questions have acceptedAnswer.text

BreadcrumbList — PASS
  ✓ 3 items with position + name

Warnings (non-blocking):
  - FAQPage: 'dateCreated' recommended for rich result eligibility
```

## CLI reference

```bash
# Validate from file
python python-backend/schema_validator.py --schema_file schema.json

# Validate inline
python python-backend/schema_validator.py --schema_json '{"@context": "https://schema.org", "@type": "FAQPage", ...}'

# Save results
python python-backend/schema_validator.py --schema_file schema.json --output validation_result.json
```
