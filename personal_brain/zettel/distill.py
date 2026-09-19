from personal_brain.core.node import BrainNode
from personal_brain.core.types import NodeType
import time

def distill_fleeting_to_permanent(fleeting_node: BrainNode, refined_title: str, permanent_content: str) -> BrainNode:
    """Converts quick raw fleeting thoughts into polished atomic permanent notes."""
    return BrainNode(
        title=refined_title,
        content=permanent_content,
        node_type=NodeType.CONCEPT,
        tags=list(set(fleeting_node.tags + ["permanent", "zettel"])),
        salience=0.8,
        metadata={"distilled_from": fleeting_node.node_id, "distilled_at": time.time()}
    )
