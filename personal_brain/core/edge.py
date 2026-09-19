from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import time
from personal_brain.core.types import EdgeType

@dataclass
class BrainEdge:
    source_id: str
    target_id: str
    edge_type: EdgeType = EdgeType.REFERENCES
    weight: float = 1.0
    label: str = ""
    created_at: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_id": self.source_id,
            "target_id": self.target_id,
            "edge_type": self.edge_type.value,
            "weight": round(self.weight, 3),
            "label": self.label,
            "created_at": self.created_at,
            "metadata": self.metadata,
        }
