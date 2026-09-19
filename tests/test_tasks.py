import unittest
from personal_brain.tasks.dag import TaskDAG
from personal_brain.tasks.toposort import topological_sort
from personal_brain.tasks.cpm import calculate_critical_path
from personal_brain.core.tasks import TaskItem

class TestTaskDAG(unittest.TestCase):
    def test_toposort_and_cpm(self):
        dag = TaskDAG()
        t1 = TaskItem("t1", "Design", estimated_hours=2.0)
        t2 = TaskItem("t2", "Develop", dependencies=["t1"], estimated_hours=4.0)
        t3 = TaskItem("t3", "Test", dependencies=["t2"], estimated_hours=1.0)
        dag.add_task(t1)
        dag.add_task(t2)
        dag.add_task(t3)
        order = topological_sort(dag)
        self.assertEqual(order, ["t1", "t2", "t3"])
        path, duration = calculate_critical_path(dag)
        self.assertEqual(duration, 7.0)

if __name__ == "__main__":
    unittest.main()
