from typing import Dict, List, Set
from personal_brain.storage.edge_repo import EdgeRepository

class AdjacencyGraph:
    def __init__(self, db_manager):
        self.db = db_manager
        self.adj: Dict[str, Set[str]] = {}
        self.in_adj: Dict[str, Set[str]] = {}
        self.build()

    def build(self):
        e_repo = EdgeRepository(self.db)
        edges = e_repo.list_all()
        for e in edges:
            if e.source_id not in self.adj:
                self.adj[e.source_id] = set()
            if e.target_id not in self.in_adj:
                self.in_adj[e.target_id] = set()
            self.adj[e.source_id].add(e.target_id)
            self.in_adj[e.target_id].add(e.source_id)

    def neighbors(self, node_id: str) -> Set[str]:
        return self.adj.get(node_id, set())

    def incoming(self, node_id: str) -> Set[str]:
        return self.in_adj.get(node_id, set())
