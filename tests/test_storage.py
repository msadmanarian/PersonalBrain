import unittest
import os
from personal_brain.storage.db import DatabaseManager
from personal_brain.storage.schema import initialize_database
from personal_brain.storage.node_repo import NodeRepository
from personal_brain.core.node import BrainNode

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager(":memory:")
        initialize_database(self.db)
        self.repo = NodeRepository(self.db)

    def test_crud(self):
        node = BrainNode(title="Alpha", content="First note", tags=["test"])
        nid = self.repo.insert(node)
        fetched = self.repo.get_by_id(nid)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.title, "Alpha")

if __name__ == "__main__":
    unittest.main()
