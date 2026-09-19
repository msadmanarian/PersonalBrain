import json
from personal_brain.core.snapshot import BrainSnapshot
from personal_brain.storage.node_repo import NodeRepository
from personal_brain.storage.edge_repo import EdgeRepository

def export_to_json(db_manager, file_path: str) -> str:
    nodes = NodeRepository(db_manager).list_all(limit=10000)
    edges = EdgeRepository(db_manager).list_all()
    snapshot = BrainSnapshot(
        nodes=[n.to_dict() for n in nodes],
        edges=[e.to_dict() for e in edges],
    )
    data = {
        "version": snapshot.version,
        "timestamp": snapshot.timestamp,
        "nodes": snapshot.nodes,
        "edges": snapshot.edges,
    }
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return file_path
