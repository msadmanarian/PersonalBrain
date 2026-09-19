from typing import Set, List
from personal_brain.graph.adjacency import AdjacencyGraph

def detect_orphan_nodes(all_node_ids: Set[str], graph: AdjacencyGraph) -> List[str]:
    """Identify isolated knowledge nodes with zero in-bound and out-bound links."""
    orphans = []
    for nid in all_node_ids:
        if not graph.neighbors(nid) and not graph.incoming(nid):
            orphans.append(nid)
    return orphans
