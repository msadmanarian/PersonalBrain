import unittest
from personal_brain.core.types import NodeType, EdgeType
from personal_brain.core.node import BrainNode
from personal_brain.core.zettel import generate_zettel_id, parse_luhmann_index

class TestCoreTypes(unittest.TestCase):
    def test_node_creation(self):
        node = BrainNode(title="Test", content="Content", node_type=NodeType.CONCEPT)
        self.assertEqual(node.title, "Test")
        self.assertEqual(node.node_type, NodeType.CONCEPT)

    def test_zettel_generator(self):
        zid = generate_zettel_id()
        self.assertEqual(len(zid), 14)

    def test_luhmann_index(self):
        tokens = parse_luhmann_index("1.1a2")
        self.assertIn("1", tokens)
        self.assertIn("a", tokens)

if __name__ == "__main__":
    unittest.main()
