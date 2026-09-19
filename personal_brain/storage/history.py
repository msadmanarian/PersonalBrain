import time
from typing import Dict, Any

class RevisionTracker:
    def __init__(self):
        self.change_log = []

    def record_change(self, node_id: str, action: str, details: Dict[str, Any]):
        self.change_log.append({
            "timestamp": time.time(),
            "node_id": node_id,
            "action": action,
            "details": details,
        })
