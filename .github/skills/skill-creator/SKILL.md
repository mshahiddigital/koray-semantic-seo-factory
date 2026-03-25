---
name: skill-creator
description: Guide for creating or updating a Codex skill folder (SKILL.md + optional scripts/references/assets) that adds specialized workflows, procedural knowledge, or tool integrations. Use when you need to design a new skill or refactor an existing one to trigger reliably and stay context-efficient.
---

# Skill Creator

## Core principles
- Keep `name` + `description` in YAML frontmatter only; do not add extra YAML fields.
- Make the **description** the primary trigger mechanism: include what the skill does and when to use it (with example user phrasing).
- Keep the SKILL.md body concise; prefer progressive disclosure (link to `references/` files) over long embedded docs.
- Match the degree of freedom to fragility:
  - High freedom: text guidance and heuristics.
  - Medium freedom: pseudocode/templates.
  - Low freedom: scripts with few parameters.

## Skill anatomy
A skill is a folder that contains a required `SKILL.md` plus optional resources:
- `scripts/`: executable code for deterministic/reusable tasks
- `references/`: documents to load only when needed
- `assets/`: templates/files used in outputs

## Writing guidelines
- Use imperative form ("Do X", "Collect inputs", "Output Y").
- Put **when to use** content in the frontmatter description, not in the body.
- Prefer short checklists and tables over paragraphs.
- Avoid deep reference chains; keep references one level deep from `SKILL.md`.

## Creation / refactor process
1. Understand usage with concrete examples (what should trigger the skill).
2. Plan reusable resources (scripts/references/assets) that reduce repeated prompting.
3. Implement/rewrite `SKILL.md`:
   - YAML: `name`, `description` only.
   - Body: workflow + outputs + references.
4. Remove stale or non-existent links and tool names.
5. Sanity-check triggering:
   - Does the description include realistic user phrasing?
   - Does the body avoid redundant background explanation?

## Progressive disclosure patterns
- Keep `SKILL.md` under ~500 lines.
- Move large catalogs, examples, or variant-specific details into `references/*.md` and link them.
- For long references (>100 lines), add a TOC at the top.
