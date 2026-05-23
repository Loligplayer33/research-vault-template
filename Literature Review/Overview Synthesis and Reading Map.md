---
title: Overview Synthesis and Reading Map
tags:
  - literature-review
  - overview
  - reading-plan
  - project
aliases:
  - Literature Overview Synthesis
  - Overview Reading Map
status: active
---

# Overview Synthesis and Reading Map

This note is the canonical cross-paper orientation for the literature review. It consolidates the reading plan, source map, and the synthesis workflow the vault uses.

## Guiding Question

**How can automated graph construction and local graph-based retrieval be optimized for highly personalized, markdown-based knowledge environments to prevent semantic drift over time?**

## Minimum Viable Reading Set

These three papers are the **absolute must-reads** that form the technical spine of the approach. Future agents should treat them as top-priority sources when applying the verdict **flag-and-ask** rule (if a must-read is downgraded to Moderate or Light, ask before producing a reading guide).

- [ ] **From Local to Global: A Graph RAG Approach to Query-Focused Summarization** (Microsoft Research / GraphRAG) — foundational GraphRAG paper
- [ ] **PROM: Personal Knowledge Graph Construction with Large Language Models** — personal knowledge graph construction from messy, everyday user text
- [ ] **PersonaAgent with GraphRAG: Community-Aware Knowledge Graphs for Personalized LLM** — user histories, preferences, and community-aware graph indexing

## Current Source Map and Reading Priority

### Must-Read Core (technical spine)

See **Minimum Viable Reading Set** above.

### Broader / Contextual

- [ ] **Beyond Static Question Banks: Dynamic Knowledge Expansion via LLM-Automated Graph Construction** — hierarchical graph building and dynamic updates; architectural ideas on graph reasoning (contextual bucket, not core spine)

## Central Themes to Track

These correspond to synthesis notes in [[Literature Review/Synthesis/README]].

### Special synthesis roles

- [[Literature Review/Synthesis/The Problem]] — information overload and structural collapse issues
- [[Literature Review/Synthesis/Design Strategies]] — concrete agent architectures
- [[Literature Review/Synthesis/Open Questions]] — where graph-based retrieval systems still drop the ball on local execution

### Cross-reading themes

- [[Literature Review/Synthesis/Graph Extraction Accuracy]] — graph extraction accuracy from unstructured text
- [[Literature Review/Synthesis/Semantic Drift Prevention]] — strategies for preventing semantic drift during continuous graph expansion
- [[Literature Review/Synthesis/Context-Awareness and Personalization]] — context-awareness and user personalization mechanisms
- [[Literature Review/Synthesis/Local Computational Overhead]] — computational overhead of running agent loops locally
- [[Literature Review/Synthesis/Human-in-the-Loop Interaction Design]] — human-in-the-loop interaction design paradigms

## Related

- [[Literature Review/README]] — full workflow guide
- [[Literature Review/Synthesis/README|Synthesis folder index]]
- [[000_Semantic_Network_Context]]
- [[001_Semantic_Network_Overview]]
