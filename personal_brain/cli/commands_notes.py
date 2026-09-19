from personal_brain.core.node import BrainNode
from personal_brain.core.types import NodeType
from personal_brain.storage.node_repo import NodeRepository

def add_note_cli(db_manager, title: str, content: str, tags: list = None) -> str:
    node = BrainNode(title=title, content=content, tags=tags or [], node_type=NodeType.NOTE)
    return NodeRepository(db_manager).insert(node)
