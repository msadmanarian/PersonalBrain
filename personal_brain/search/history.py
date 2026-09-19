import time
from typing import List, Dict, Any

class SearchHistory:
    def __init__(self, max_history: int = 50):
        self.history = []
        self.max_history = max_history

    def log_query(self, query: str, result_count: int):
        self.history.append({
            "query": query,
            "result_count": result_count,
            "timestamp": time.time(),
        })
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def get_recent(self) -> List[str]:
        return [h["query"] for h in reversed(self.history[-10:])]
