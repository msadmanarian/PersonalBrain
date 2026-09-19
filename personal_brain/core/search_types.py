from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class SearchResult:
    node_id: str
    title: str
    snippet: str
    score: float
    match_type: str = "bm25"

@dataclass
class SerendipityMatch:
    source_node_id: str
    source_title: str
    target_node_id: str
    target_title: str
    associative_bridge: str
    affinity_score: float
