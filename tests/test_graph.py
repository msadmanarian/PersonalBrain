import unittest
from personal_brain.graph.wikilinks import extract_wikilinks
from personal_brain.graph.pagerank import compute_pagerank

class TestGraphAlgorithms(unittest.TestCase):
    def test_wikilinks_extraction(self):
        text = "This links to [[Cognitive Science]] and [[Zettelkasten|PKM]]."
        links = extract_wikilinks(text)
        self.assertEqual(len(links), 2)
        self.assertIn("Cognitive Science", links)

    def test_pagerank(self):
        nodes = {"A", "B", "C"}
        adj = {"A": {"B", "C"}, "B": {"C"}, "C": {"A"}}
        ranks = compute_pagerank(nodes, adj)
        self.assertEqual(len(ranks), 3)
        self.assertAlmostEqual(sum(ranks.values()), 1.0, places=2)

if __name__ == "__main__":
    unittest.main()
