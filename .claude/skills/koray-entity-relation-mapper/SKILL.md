---
name: koray-entity-relation-mapper
description: Build a complete entity relation map for a niche or page — identifying the central entity, all related entities, their relation types (hypernym, hyponym, meronym, causal, temporal, associative), and how they connect to form a semantic content network. Use for requests like "entity map", "entity relations", "entity graph", "conceptual relations", "what entities are connected", "central entity for [topic]", or "knowledge graph structure".
---

# Koray Entity Relation Mapper

## Relation types to map

- **Hypernym** — the broader category (Electric Scooter → Personal Mobility Device)
- **Hyponym** — the narrower type (Electric Scooter → Foldable Electric Scooter)
- **Meronym** — a part of the entity (Electric Scooter → Battery, Motor, Frame)
- **Holonym** — the entity is a part of (Electric Scooter → Urban Transport System)
- **Causal** — causes or is caused by (Battery Capacity → Range)
- **Temporal** — precedes or follows (Purchase → Registration → Use)
- **Associative** — commonly co-occurs with (Electric Scooter → Charging Station, Helmet)
- **Comparative** — contrasted with (Electric Scooter vs. Electric Bike)

## Workflow

1. Collect inputs: central entity, niche/domain, target country, topical map (if available).
2. Define the central entity precisely (name, definition, source context in 1–2 sentences).
3. List all related entities (target 15–30 for a full niche map).
4. Assign relation types to each entity pair.
5. Identify which relations map to Core pages vs Outer pages in the topical structure.
6. Flag entities with high commercial value (likely Core) vs historical/support value (likely Outer).
7. Output a Mermaid diagram spec + a flat relation table.

## Output

- **Central entity definition** (1–2 sentences with source context)
- **Entity relation table**: `Entity | Relation type | Related entity | Section (Core/Outer) | Priority`
- **Mermaid diagram** (entity graph — nodes = entities, edges = relation type labels)
- **Content implications**: which relations suggest new pages, new sections, or new EAV attributes

## References (load only if needed)

- `references/eav-modeling-guide.md`
