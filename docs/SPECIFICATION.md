# PersonalBrain System Specification

## 1. Overview
PersonalBrain is a local-first, cognitive exocortex uniting bi-directional associative knowledge graphs, SuperMemo-2 spaced repetition, and Directed Acyclic Graph (DAG) task scheduling.

## 2. Architecture Layers
1. **Core Domain Primitives**: Strongly typed nodes, edges, Zettel identifiers.
2. **Persistence Engine**: SQLite with Write-Ahead Logging (WAL) and JSON backup.
3. **Graph Theory Engine**: Adjacency models, PageRank centrality, cluster analysis.
4. **Cognitive Retention Engine**: SM-2 and FSRS algorithms.
5. **Hierarchical Task Engine**: DAG scheduler and Critical Path Method.
6. **Hybrid Retrieval**: Inverted index BM25 combined with sparse TF-IDF vectors.
