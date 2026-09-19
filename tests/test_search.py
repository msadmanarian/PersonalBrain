import unittest
from personal_brain.search.bm25 import BM25Ranker

class TestSearch(unittest.TestCase):
    def test_bm25(self):
        docs = {
            "d1": "PersonalBrain is an AI exocortex for knowledge management",
            "d2": "Spaced repetition uses SM-2 algorithm for memory retention",
        }
        ranker = BM25Ranker()
        ranker.fit(docs)
        results = ranker.score("exocortex knowledge")
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0][0], "d1")

if __name__ == "__main__":
    unittest.main()
