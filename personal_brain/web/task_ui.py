from typing import List, Dict, Any

def render_task_kanban_columns(tasks: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    columns = {"inbox": [], "next": [], "in_progress": [], "done": []}
    for t in tasks:
        state = t.get("state", "inbox")
        if state in columns:
            columns[state].append(t)
    return columns
