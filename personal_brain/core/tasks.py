from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional
import time

class TaskState(str, Enum):
    INBOX = "inbox"
    NEXT = "next"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
    REVIEW = "review"
    DONE = "done"

class Priority(int, Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

@dataclass
class TaskItem:
    task_id: str
    title: str
    state: TaskState = TaskState.INBOX
    priority: Priority = Priority.MEDIUM
    estimated_hours: float = 1.0
    dependencies: List[str] = field(default_factory=list)
    due_date: Optional[float] = None
    created_at: float = field(default_factory=time.time)
    completed_at: Optional[float] = None
