from typing import List, Dict
from personal_brain.core.node import BrainNode

def get_nodes_by_tag(db_manager, tag: str) -> List[BrainNode]:
    from personal_brain.storage.node_repo import NodeRepository
    all_nodes = NodeRepository(db_manager).list_all(limit=5000)
    tag_clean = tag.strip().lower()
    return [n for n in all_nodes if tag_clean in [t.lower() for t in n.tags]]
