import json
from personal_brain.core.node import BrainNode
from personal_brain.core.edge import BrainEdge
from personal_brain.core.types import NodeType, EdgeType
from personal_brain.storage.node_repo import NodeRepository
from personal_brain.storage.edge_repo import EdgeRepository

def restore_from_json(db_manager, file_path: str) -> int:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    n_repo = NodeRepository(db_manager)
    e_repo = EdgeRepository(db_manager)
    count = 0
    with db_manager.conn:
        for n_data in data.get("nodes", []):
            node = BrainNode.from_dict(n_data)
            n_repo.insert(node)
            count += 1
        for e_data in data.get("edges", []):
            edge = BrainEdge(
                source_id=e_data["source_id"],
                target_id=e_data["target_id"],
                edge_type=EdgeType(e_data.get("edge_type", "references")),
                weight=e_data.get("weight", 1.0),
                label=e_data.get("label", ""),
            )
            e_repo.insert(edge)
    return count
