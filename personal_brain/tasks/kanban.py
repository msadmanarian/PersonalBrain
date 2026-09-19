from personal_brain.core.tasks import TaskItem, TaskState
import time

VALID_TRANSITIONS = {
    TaskState.INBOX: {TaskState.NEXT, TaskState.BLOCKED},
    TaskState.NEXT: {TaskState.IN_PROGRESS, TaskState.BLOCKED},
    TaskState.IN_PROGRESS: {TaskState.REVIEW, TaskState.BLOCKED, TaskState.DONE},
    TaskState.BLOCKED: {TaskState.NEXT, TaskState.IN_PROGRESS},
    TaskState.REVIEW: {TaskState.DONE, TaskState.IN_PROGRESS},
    TaskState.DONE: {TaskState.INBOX},
}

def transition_task_state(task: TaskItem, new_state: TaskState) -> bool:
    if new_state in VALID_TRANSITIONS.get(task.state, set()):
        task.state = new_state
        if new_state == TaskState.DONE:
            task.completed_at = time.time()
        return True
    return False
