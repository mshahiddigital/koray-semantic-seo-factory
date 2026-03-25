---
name: koray-e-e-a-t-entity-builder
description: Build and audit E-E-A-T (Experience, Expertise, Authority, Trustworthiness) signals for a site or page — covering author entity markup, organizational identity, about/contact pages, credentials, trust signals, and policy pages. Use for requests like "E-E-A-T signals", "build trust signals", "author entity", "about page optimization", "Google trust", "who-is-responsible signals", "YMYL trust", or "E-E-A-T audit".
---

# Koray E-E-A-T Entity Builder

## E-E-A-T signal categories

**Experience**

- First-hand experience signals: "I/we have used/tested/visited..." statements with specifics
- Case studies, real data, dated observations
- Photos, video, operational proof

**Expertise**

- Author entity: name, credentials, role, verifiable online presence (LinkedIn, social)
- Author bylines on every article/service page
- Source context on every factual claim ("According to [authority]...")
- Specialty depth: does the page answer questions only an expert would know to address?

**Authority**

- Organization entity: legal name, registered address, founding date, team
- Third-party mentions/citations/backlinks (signal of external recognition)
- Industry association memberships, certifications, licenses

**Trustworthiness**

- Contact page: real address, phone, email, map embed
- Privacy policy, terms of service, refund/cancellation policy
- Secure HTTPS, clear ownership
- Transparent pricing (no hidden fees — state constraints explicitly)
- Review/testimonial evidence with names and dates

## Workflow

1. Identify the site type (YMYL = highest bar; informational = lower bar; local service = medium).
2. Audit current E-E-A-T signals for each category (score 0–25 per category = 100 total).
3. Identify missing signals by priority (P0 = trust blockers, P1 = authority gaps, P2 = depth).
4. Generate the required pages/content:
   - About page brief (author + organization entity markup)
   - Author bio template (structured for `Person` schema)
   - `Organization` JSON-LD block
   - Trust signal checklist per page type

## Output

- **E-E-A-T audit score**: `Category | Score (0–25) | Key gaps`
- **Total score** (0–100) with benchmark: < 60 = high HCU risk
- **Missing signal plan**: `Signal | Page/section | Content needed | Priority`
- **About page brief** (entity-focused, with `Person` + `Organization` schema)
- **JSON-LD block** for `Organization` and primary `Person` author entity
- **Trust signal checklist** (per page type)

## References (load only if needed)

- `references/hcu-signals-checklist.md`
