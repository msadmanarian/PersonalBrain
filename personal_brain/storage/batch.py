from typing import List
from personal_brain.core.node import BrainNode
from personal_brain.core.edge import BrainEdge

def batch_insert(db_manager, nodes: List[BrainNode], edges: List[BrainEdge]) -> None:
    from personal_brain.storage.node_repo import NodeRepository
    from personal_brain.storage.edge_repo import EdgeRepository
    n_repo = NodeRepository(db_manager)
    e_repo = EdgeRepository(db_manager)
    with db_manager.conn:
        for node in nodes:
            n_repo.insert(node)
        for edge in edges:
            e_repo.insert(edge)
