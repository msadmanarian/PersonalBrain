from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import time
import uuid
from personal_brain.core.types import NodeType

@dataclass
class BrainNode:
    title: str
    content: str
    node_type: NodeType = NodeType.NOTE
    node_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    tags: List[str] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)
    salience: float = 0.5

    def to_dict(self) -> Dict[str, Any]:
        return {
            "node_id": self.node_id,
            "title": self.title,
            "content": self.content,
            "node_type": self.node_type.value,
            "tags": self.tags,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "metadata": self.metadata,
            "salience": round(self.salience, 3),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BrainNode":
        return cls(
            node_id=data.get("node_id", str(uuid.uuid4())[:8]),
            title=data.get("title", "Untitled"),
            content=data.get("content", ""),
            node_type=NodeType(data.get("node_type", "note")),
            tags=data.get("tags", []),
            created_at=data.get("created_at", time.time()),
            updated_at=data.get("updated_at", time.time()),
            metadata=data.get("metadata", {}),
            salience=data.get("salience", 0.5),
        )
