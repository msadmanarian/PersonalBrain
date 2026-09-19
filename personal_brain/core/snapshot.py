from dataclasses import dataclass, field
from typing import List, Dict, Any
import time

@dataclass
class BrainSnapshot:
    version: str = "1.0.0"
    timestamp: float = field(default_factory=time.time)
    nodes: List[Dict[str, Any]] = field(default_factory=list)
    edges: List[Dict[str, Any]] = field(default_factory=list)
    tasks: List[Dict[str, Any]] = field(default_factory=list)
    cards: List[Dict[str, Any]] = field(default_factory=list)
