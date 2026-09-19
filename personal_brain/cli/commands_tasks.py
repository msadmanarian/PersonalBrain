from personal_brain.tasks.dag import TaskDAG
from personal_brain.tasks.cpm import calculate_critical_path

def evaluate_tasks_cli(tasks: list):
    dag = TaskDAG()
    for t in tasks:
        dag.add_task(t)
    return calculate_critical_path(dag)
