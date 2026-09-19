from typing import Dict, List, Set
from personal_brain.core.tasks import TaskItem

class TaskDAG:
    def __init__(self):
        self.tasks: Dict[str, TaskItem] = {}
        self.adj: Dict[str, Set[str]] = {}
        self.in_adj: Dict[str, Set[str]] = {}

    def add_task(self, task: TaskItem):
        self.tasks[task.task_id] = task
        if task.task_id not in self.adj:
            self.adj[task.task_id] = set()
        if task.task_id not in self.in_adj:
            self.in_adj[task.task_id] = set()
        for dep in task.dependencies:
            if dep not in self.adj:
                self.adj[dep] = set()
            self.adj[dep].add(task.task_id)
            self.in_adj[task.task_id].add(dep)
