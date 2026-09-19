from dataclasses import dataclass, field
from typing import Dict, Any, List

@dataclass
class GraphMetrics:
    total_nodes: int = 0
    total_edges: int = 0
    orphan_count: int = 0
    cluster_count: int = 0
    density: float = 0.0
    avg_degree: float = 0.0
    diameter: int = 0
    top_central_nodes: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "total_nodes": self.total_nodes,
            "total_edges": self.total_edges,
            "orphan_count": self.orphan_count,
            "cluster_count": self.cluster_count,
            "density": round(self.density, 4),
            "avg_degree": round(self.avg_degree, 2),
            "top_central_nodes": self.top_central_nodes,
        }
