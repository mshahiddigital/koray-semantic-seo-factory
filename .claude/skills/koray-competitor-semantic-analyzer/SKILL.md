---
name: koray-competitor-semantic-analyzer
description: Perform a deep semantic diff between your content/topical map and top competitors — comparing EAV coverage, lexical gaps, entity prominence, heading structure, and query overlap. Use for requests like "competitor analysis", "semantic diff", "what are competitors covering that we aren't", "compare our EAV to competitor", or "information gain vs competitor".
---

# Koray Competitor Semantic Analyzer

## Workflow

1. Collect inputs: your page/site (file path, URL, or pasted content) + 2–5 competitor URLs or headings.
2. Extract entities and EAV triples from each source:
   - Your content: identify central entity, attributes covered, values provided, source context.
   - Each competitor: extract headings, entities, attributes, FAQs, and any unique EAV triples.
3. Build the semantic diff table:
   - EAV triples you have that competitors lack (your unique information gain).
   - EAV triples competitors have that you lack (your gaps).
   - Lexical coverage: synonyms, hypernyms, and related terms competitors use that you don't.
4. Score information gain per gap: estimate impact using query intent + EAV uniqueness.
5. Prioritize gaps: P0 (your page fails task completion) → P1 (high-intent missing) → P2 (depth additions).
6. Map each gap to a recommended action (new section, new page, brief update, internal link).

## Output

- **Your unique EAV** (what you have that competitors lack — strengths to amplify)
- **Gap table**: `Missing EAV / Entity | Competitor source | Recommended fix | Priority`
- **Lexical gap list** (terms, synonyms, hypernyms competitors use — you should integrate)
- **Heading structure comparison** (which intents competitors address that you don't)
- **Action plan**: `Action | Target page/section | Priority`

## Quality bar

- Base every gap on actual content evidence — no speculation.
- Flag gaps with "Unknown" if competitor content is unavailable.
- Focus on information gain, not keyword stuffing.
