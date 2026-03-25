# Koray Semantic SEO Factory

A multi-agent AI system built on [Claude Code](https://claude.ai/code) that implements Koray Tugberk Gubur's semantic SEO framework for building unbreakable Topical Authority.

The factory automates the entire semantic SEO pipeline — from niche research and topical mapping through content brief generation, holistic writing, quality auditing, schema markup, and WordPress deployment — using 69 specialized AI agents and 23 Claude Code skills working in parallel.

---

## Table of Contents

- [Core Concept](#core-concept)
- [Architecture](#architecture)
- [Agent Tiers](#agent-tiers)
- [Skills](#skills)
- [Python Backend](#python-backend)
- [Reference Documents](#reference-documents)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Workflow Phases](#workflow-phases)
- [Topical Authority Formula](#topical-authority-formula)
- [The 42 Writing Rules](#the-42-writing-rules)
- [Deployment](#deployment)
- [Requirements](#requirements)
- [License](#license)

---

## Core Concept

Every page, brief, and audit in this system is governed by Koray Tugberk Gubur's Topical Authority formula:

```
Topical Authority = Coverage x Historical Data x Cost of Retrieval + Momentum + Depth + Vastness + Updateness
```

The factory treats SEO content as a **semantic engineering problem** — not keyword stuffing. Every page is built around Entity-Attribute-Value (EAV) triples, every claim carries source context, and every internal link follows exact-title anchor text matching.

---

## Architecture

```
koray-seo-factory/
├── .claude/
│   ├── agents/          # 69 specialized AI agents (AGENT.md each)
│   ├── skills/          # 23 Claude Code skills (SKILL.md each)
│   └── CLAUDE.md        # System instructions for the orchestrator
├── references/          # Shared knowledge base (writing rules, formulas, guides)
├── python-backend/      # 17 Python scripts for SEO automation
├── projects/            # Per-niche workspaces with all deliverables
│   └── <niche-slug>/
│       ├── research/    # Topical maps, query networks, research sheets
│       ├── briefs/      # One EAV brief per planned page
│       ├── content/     # Optimized page drafts (Markdown)
│       ├── network/     # Internal linking plans, publishing schedules
│       ├── audit/       # HCU quality audit reports per page
│       └── sheets/      # CSV tracking sheets (master, EAV, links)
└── README.md
```

---

## Agent Tiers

The system uses a 3-tier agent hierarchy where higher tiers coordinate lower tiers:

### Tier 1 — Orchestration Agents (14 agents)

Coordinate workflow phases, spawn subordinate agents, and gate deliverables.

| Agent | Role |
|-------|------|
| `koray-orchestrator-agent` | Full project run master — coordinates all phases |
| `koray-researcher-agent` | Query network building + semantic gap analysis |
| `koray-mapper-agent` | Topical map construction + coverage scoring |
| `koray-brief-generator-agent` | EAV content briefs per page (batches of 5-10) |
| `koray-network-planner-agent` | Hub/spoke internal linking architecture |
| `koray-writer-agent` | 42-rule holistic writing + optimization |
| `koray-auditor-agent` | HCU quality audit scoring (0-100) |
| `koray-python-engineer-agent` | Python SEO script execution |
| `core-update-simulator` | Google algorithm update impact simulation |
| `gsc-trend-forecaster` | Google Search Console trend projection |
| `hcu-impact-analyzer` | Helpful Content Update portfolio assessment |
| `momentum-depth-analyzer` | Momentum + Depth TA component scoring |
| `rapid-iteration-planner` | Sprint planning after audit failures |
| `topical-authority-forecaster` | 30/60/90-day TA score forecasting |

### Tier 2 — Task Agents (42 agents)

Execute bounded workflow steps at page or section level.

| Agent | Function |
|-------|----------|
| `bridge-topic-suggester` | Find topics connecting Core to Outer sections |
| `cannibalization-resolver` | Detect + resolve keyword cannibalization |
| `central-entity-identifier` | Define the central entity + disambiguation |
| `competitor-publishing-velocity-tracker` | Track competitor publishing rate |
| `competitor-semantic-diff-tool` | EAV diff vs competitor pages |
| `conceptual-relation-mapper` | Map abstract entity relations |
| `configuration-sheet-generator` | Generate master tracking CSV |
| `configuration-sheet-auditor` | Audit master_sheet.csv for failures |
| `cost-of-retrieval-estimator` | Score Cost of Retrieval (0-100) |
| `crawl-budget-semantic-optimizer` | Fix CoR issues in HTML + structure |
| `eav-triple-generator-advanced` | Generate 15+ enriched EAV triples |
| `entity-disambiguation-validator` | Validate entity disambiguation signals |
| `entity-prominence-scorer` | Score entity prominence in page structure |
| `entity-relation-graph-builder` | Build entity relation graph (Mermaid) |
| `frame-semantics-extractor` | Apply FrameNet for semantic gaps |
| `information-gain-extractor` | Extract unique EAV triples vs competitors |
| `information-gain-scorer` | Score uniqueness x relevance x depth |
| `intent-drift-detector` | Detect semantic drift from target cluster |
| `internal-linking-gap-finder` | Find missing links + orphan pages |
| `internal-linking-matrix-builder` | Build link adjacency matrix |
| `knowledge-domain-classifier` | Classify page domain + E-E-A-T level |
| `knowledge-graph-entity-optimizer` | Optimize for Google Knowledge Graph |
| `lexical-relations-builder` | Build full lexical relation inventory |
| `micro-semantics-auditor` | Sentence-level semantic quality pass |
| `paragraph-function-optimizer` | Enforce claim-evidence-implication |
| `passage-ranking-readiness-auditor` | Audit sections for passage ranking |
| `programmatic-page-templater` | Build reusable Jinja/Markdown templates |
| `query-network-visualizer` | Generate Mermaid query topology maps |
| `schema-markup-creator` | Generate JSON-LD schema blocks |
| `schema-readiness-auditor` | Audit schema for rich results |
| `sentiment-structure-analyzer` | Audit Rules 17+18 sentiment arc |
| `serps-second-by-second-tracker` | Monitor SERP volatility |
| `source-context-reinforcer` | Enforce claim source attribution |
| `topical-coverage-calculator` | Calculate Coverage TA component |
| `topical-gap-monitor` | Monitor competitor EAV additions |
| `update-frequency-scheduler` | Build content update calendar |
| `user-behavior-proxy-modeler` | Model behavioral signals |
| `user-segment-entity-matcher` | Match user segments to EAV needs |
| `vastness-updateness-scorer` | Score Vastness + Updateness |
| `wp-deploy-agent` | Deploy pages to WordPress via REST API |
| `browser-qa-agent` | Post-deploy technical SEO QA |
| `new-site-builder` | Build new WordPress or Next.js sites |

### Tier 3 — Micro-Rule Enforcer Agents (13 agents)

Apply individual Koray writing rules at sentence, word, or element level.

| Agent | Rule Enforced |
|-------|---------------|
| `bold-answer-enforcer` | Rule 10 — bold the factual answer, never the keyword |
| `final-polish-agent` | Rule 41 — read-aloud test + full 42-rule compliance |
| `heading-vector-aligner` | Rule 23 — heading matches query intent semantically |
| `list-optimization-enforcer` | Rule 26 — lists need purpose sentence, max 7 items |
| `list-pos-consistency-enforcer` | Rule 8 — all list items use same part of speech |
| `negative-phrase-remover` | Rule 17 — no negative phrases; rewrite as positive |
| `pos-consistency-checker` | Rule 8 — full-document POS consistency audit |
| `safe-answer-generator` | Rule 24 — rewrite overpromising claims as evidence-based |
| `semantic-html-generator` | Generate semantic HTML5 landmark structure |
| `semantic-role-labeler` | Rules 1+6 — entity in subject position, precise verbs |
| `subordinate-text-optimizer` | Rule 16 — sub-section openings are self-contained |
| `verb-of-life-flow-builder` | Rule 20 — verbs follow user's real-world journey |
| `word-sequence-optimizer` | Rule 1 — most important information first |

---

## Skills

23 slash-command skills provide high-level workflows that users invoke directly:

| Skill | Purpose |
|-------|---------|
| `/koray-master-semantic-seo-orchestrator` | Full end-to-end project run |
| `/koray-topical-map-architect` | Build core/outer topical map |
| `/koray-query-network-gap-researcher` | Query clusters + gap analysis |
| `/koray-eav-triple-semantic-brief-generator` | EAV briefs per page |
| `/koray-semantic-content-network-planner` | Hub/spoke internal linking |
| `/koray-holistic-writing-optimizer` | 42-rule writing optimization |
| `/koray-hcu-quality-auditor` | Scored HCU quality audit (0-100) |
| `/koray-python-seo-scripter` | Run Python SEO scripts |
| `/koray-topical-authority-scorer` | Numeric TA formula score |
| `/koray-competitor-semantic-analyzer` | EAV + lexical diff vs competitors |
| `/koray-entity-relation-mapper` | Entity graph + relation types |
| `/koray-e-e-a-t-entity-builder` | E-E-A-T signals + author entity markup |
| `/koray-schema-markup-creator` | JSON-LD structured data |
| `/koray-crawl-budget-semantic-optimizer` | Cost of retrieval + HTML semantics |
| `/koray-content-calendar-planner` | 30/60/90-day publishing calendar |
| `/koray-configuration-sheet-manager` | Master tracking sheet (CSV) |
| `/koray-dashboard-generator` | Google Sheets / Looker Studio spec |
| `/koray-algorithm-adapter` | Traffic drop diagnosis + fix plan |
| `/koray-real-time-trend-monitor` | SERP + competitor shift tracking |
| `/koray-programmatic-page-generator` | Bulk page templates + CSV |
| `/koray-patent-researcher` | Google patent to SEO action translation |
| `/validate-schema` | JSON-LD schema validation |
| `/wp-deploy` | WordPress REST API deployment |

---

## Python Backend

17 automation scripts in `python-backend/` handle data processing tasks:

| Script | Function |
|--------|----------|
| `entity_extractor.py` | Extract entities from text using NLP |
| `query_clusterer.py` | Cluster queries by semantic similarity |
| `topicality_scorer.py` | Score topical relevance of content |
| `eav_triple_generator.py` | Generate EAV triples from text |
| `semantic_similarity_calculator.py` | Calculate cosine similarity between texts |
| `serp_scraper.py` | Scrape SERP results for analysis |
| `coverage_auditor.py` | Audit topical coverage completeness |
| `gap_report_pipeline.py` | Generate gap analysis reports |
| `agent_orchestrator.py` | Orchestrate Python agent workflows |
| `research_compiler.py` | Compile research into structured sheets |
| `dashboard_generator.py` | Generate dashboard specifications |
| `patent_scraper.py` | Scrape and parse Google patents |
| `schema_validator.py` | Validate JSON-LD schema markup |
| `wp_deployer.py` | Deploy content to WordPress via REST API |
| `browser_qa.py` | Run browser-based QA checks |
| `nextjs_page_builder.py` | Generate Next.js page components |

---

## Reference Documents

Shared knowledge files in `references/` that agents and skills load:

| File | Contents |
|------|----------|
| `koray-writing-rules.md` | All 42 holistic writing rules with checklist |
| `topical-authority-formula.md` | TA formula breakdown with scoring guide |
| `eav-modeling-guide.md` | Entity-Attribute-Value triple modeling guide |
| `core-outer-examples.md` | Core vs Outer section structure examples |
| `hcu-signals-checklist.md` | Helpful Content Update signals checklist |
| `query-network-best-practices.md` | Query network clustering best practices |

---

## Project Structure

Each niche gets its own workspace under `projects/<niche-slug>/`:

```
projects/<niche-slug>/
├── research/
│   ├── topical-map.md          # Core/Outer hierarchy with entities
│   ├── query-network-gaps.md   # Query clusters + coverage gaps
│   └── research_sheet.csv      # Compiled research data
├── briefs/
│   └── <page-slug>.md          # EAV brief per planned page
├── content/
│   └── <page-slug>.md          # Optimized page draft (Markdown)
├── network/
│   ├── internal-linking-plan.md # Hub/spoke link architecture
│   └── publishing-plan.md      # Sequenced publishing calendar
├── audit/
│   └── hcu-quality-audit.md    # HCU score per page (must be >= 80)
├── sheets/
│   ├── master_sheet.csv        # Master tracking sheet
│   ├── entities_eav.csv        # All EAV triples
│   └── internal_links.csv      # Link adjacency matrix
└── scripts/                    # Niche-specific automation scripts
```

---

## Getting Started

### Prerequisites

- [Claude Code CLI](https://claude.ai/code) installed and authenticated
- Python 3.10+ (for backend scripts)
- Git

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mshahiddigital/koray-semantic-seo-factory.git
   cd koray-semantic-seo-factory
   ```

2. **Open in Claude Code:**
   ```bash
   claude
   ```

3. **Start a new project:**
   ```
   Run the full Koray workflow for [your niche]
   ```
   Or use individual skills:
   ```
   /koray-topical-map-architect for [your niche]
   ```

### Quick Start Example

```
User: Build topical authority for "electric scooters" targeting Australia

Claude Code will automatically:
1. Spawn researcher + mapper agents in parallel
2. Build query network + topical map
3. Generate EAV briefs for each page
4. Write optimized content using all 42 rules
5. Audit every page (must score >= 80)
6. Output everything to projects/electric-scooters/
```

---

## Workflow Phases

The factory executes in strict parallel phases:

### Phase 1 — Research (parallel)
- `koray-researcher-agent` builds query network + gap list
- `koray-mapper-agent` builds topical map + coverage score

### Phase 2 — Planning (parallel, after Phase 1)
- `koray-network-planner-agent` creates internal linking plan
- `koray-brief-generator-agent` generates EAV briefs (batches of 5-10)

### Phase 3 — Production (parallel, after Phase 2)
- `koray-writer-agent` writes + optimizes pages using 42 rules
- `koray-python-engineer-agent` runs automation scripts

### Phase 4 — Quality Gate (after Phase 3)
- `koray-auditor-agent` scores every page (0-100)
- Pages scoring < 80 return to the writer for fixes
- Pages scoring >= 80 are ship-ready

### Phase 5 — Deployment (optional)
- `wp-deploy-agent` deploys to WordPress via REST API
- `browser-qa-agent` runs post-deploy technical SEO QA

---

## Topical Authority Formula

Each component is scored 0-100 with weighted contribution:

| Component | Weight | What It Measures |
|-----------|--------|------------------|
| **Coverage** | 30% | Semantic completeness of EAV triples, query networks, lexical relations |
| **Historical Data** | 20% | Site/page age, update history, backlinks over time |
| **Cost of Retrieval** | 20% | Semantic HTML, structured data, crawl efficiency |
| **Momentum** | 10% | Traffic/engagement growth curves |
| **Depth** | 10% | Detailed EAV attributes per entity, paragraph depth |
| **Vastness** | 5% | Breadth of related entities and outer topics |
| **Updateness** | 5% | Content freshness signals and update frequency |

**Target:** 85+ for "unbreakable" topical authority in a niche.

---

## The 42 Writing Rules

Every page passes through all 42 of Koray's holistic writing rules:

### 14 Core Rules (every sentence)
1. Proper word sequence — most important information first
2. Be certain and factual — no "should", "might", "probably"
3. Cut all fluff and metadiscourse
4. Use numeric values and qualifiers
5. Qualify instances with concrete examples
6. Correct verb context — precise verbs only
7. Examples after plural nouns
8. Same part-of-speech consistency in lists
9. Immediate answer under every heading (first 30-45 words)
10. Bold the answer, not the search term
11. One macro context per page
12. "If" condition first, result second
13. Anchor text matches target page title exactly
14. Weave EAV triples and lexical relations naturally

### 28 Advanced Patterns (micro-semantics)
15-42 cover paragraph function optimization, subordinate text rules, positive sentiment, EAV integration, verbs-of-life flow, source context, information gain, heading alignment, safe answers, numeric density, list optimization, internal linking, schema readiness, readability, historical data signals, user behavior alignment, momentum building, depth layering, vastness support, updateness, evidence-based writing, algorithmic authorship, final polish, and HCU compliance.

See [`references/koray-writing-rules.md`](references/koray-writing-rules.md) for the complete rule set with examples.

---

## Deployment

### WordPress Deployment
```
/wp-deploy for [page-slug] to [your-site.com]
```
The `wp-deploy-agent` handles:
- Schema validation before deployment
- Internal link injection
- SEO meta fields (Rank Math or Yoast)
- Draft publishing with edit/preview links

### Schema Validation
```
/validate-schema for [page-slug]
```
Validates JSON-LD against Google's requirements before deployment.

---

## Requirements

- **Claude Code CLI** — primary runtime for all agents and skills
- **Python 3.10+** — for backend automation scripts
- **Optional:** WordPress 6.9+ site for deployment via REST API
- **Optional:** Google Search Console export for trend analysis

---

## Non-Negotiable Quality Gates

- All 42 writing rules must pass on every page
- One macro context per page — no topic jumping
- Minimum 10 EAV triples per brief
- Core vs Outer section structure enforced
- Source context required on every factual claim
- Anchor text = exact destination page title
- **HCU score >= 80** before any page ships

---

## Author

Built by [M Shahid Digital](https://github.com/mshahiddigital) using the Koray Tugberk Gubur Semantic SEO framework.

---

## License

This project is proprietary. All rights reserved.
