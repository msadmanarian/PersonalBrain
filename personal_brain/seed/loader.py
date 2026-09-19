from personal_brain.seed.cs_foundations import CS_NODES
from personal_brain.seed.ai_cognition import AI_NODES
from personal_brain.seed.distributed_systems import DISTRIBUTED_NODES
from personal_brain.seed.philosophy import PHILOSOPHY_NODES
from personal_brain.seed.productivity import PRODUCTIVITY_NODES
from personal_brain.storage.node_repo import NodeRepository
from personal_brain.storage.edge_repo import EdgeRepository
from personal_brain.core.edge import BrainEdge
from personal_brain.core.types import EdgeType
from personal_brain.graph.wikilinks import extract_wikilinks

def seed_knowledge_base(db_manager) -> int:
    n_repo = NodeRepository(db_manager)
    e_repo = EdgeRepository(db_manager)
    all_seeds = CS_NODES + AI_NODES + DISTRIBUTED_NODES + PHILOSOPHY_NODES + PRODUCTIVITY_NODES
    title_to_id = {}
    for node in all_seeds:
        n_repo.insert(node)
        title_to_id[node.title.lower()] = node.node_id
    # Auto-link based on wikilinks
    edge_count = 0
    for node in all_seeds:
        targets = extract_wikilinks(node.content)
        for t in targets:
            tgt_id = title_to_id.get(t.lower())
            if tgt_id and tgt_id != node.node_id:
                edge = BrainEdge(source_id=node.node_id, target_id=tgt_id, edge_type=EdgeType.REFERENCES)
                e_repo.insert(edge)
                edge_count += 1
    return len(all_seeds)
