from typing import Dict, List, Set
from personal_brain.storage.edge_repo import EdgeRepository
from personal_brain.storage.node_repo import NodeRepository
from personal_brain.core.node import BrainNode

def resolve_backlinks(db_manager, node_id: str) -> List[BrainNode]:
    """Retrieve all nodes that link inbound to the target node."""
    e_repo = EdgeRepository(db_manager)
    n_repo = NodeRepository(db_manager)
    inbound_edges = e_repo.get_inbound(node_id)
    backlinked_nodes = []
    for edge in inbound_edges:
        node = n_repo.get_by_id(edge.source_id)
        if node:
            backlinked_nodes.append(node)
    return backlinked_nodes
