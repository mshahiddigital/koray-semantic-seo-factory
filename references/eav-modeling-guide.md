# Koray EAV Modeling Guide v2.1
**Author:** Koray Tuğberk Gübür (Holistic SEO) + Enhanced for Claude Skills  
**Version:** 2.1 – February 2026  
**Purpose:** Loaded by Brief Generator and Writer agents for precise entity optimization.

## Core Concepts
- **EAV Triple:** Entity (subject) | Attribute (property) | Value (description/data).
- **Semantic Triple:** Subject-Predicate-Object (extends EAV for relations).
- Always include Source Context (authority/study/patent).

## Step-by-Step Modeling
1. Identify Central Entity (e.g., "Electric Scooter").
2. List Attributes (e.g., Battery Life, Top Speed, Price Range).
3. Assign Values (e.g., 20–40 km, 25–50 km/h, $200–$800).
4. Add Relations (e.g., "Electric Scooter" – manufactured by – "Xiaomi").

## Output Template (Markdown Table)
| Entity          | Attribute     | Value          | Source Context |
|-----------------|---------------|----------------|----------------|
| Electric Scooter| Battery Life | 20–40 km      | Xiaomi Specs 2026 |

## Best Practices
- Minimum 5–10 EAV per page.
- Integrate naturally: "The Xiaomi Mi Electric Scooter offers a battery life of 30 km, ideal for urban commuting."
- Use Python for extraction: NLTK/spaCy for auto-EAV from text.

Examples:
- For "Visa Germany": Entity=Student Visa | Attribute=Duration | Value=Up to 4 years | Source=German Embassy.

Last updated: February 17, 2026