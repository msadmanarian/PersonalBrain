import unittest
from personal_brain.memory.sm2 import calculate_sm2
from personal_brain.memory.flashcards import extract_flashcards_from_markdown

class TestMemoryEngine(unittest.TestCase):
    def test_sm2_progression(self):
        reps, ef, interval = calculate_sm2(0, 2.5, 1.0, 5)
        self.assertEqual(reps, 1)
        self.assertEqual(interval, 1.0)
        reps2, ef2, interval2 = calculate_sm2(reps, ef, interval, 4)
        self.assertEqual(reps2, 2)
        self.assertEqual(interval2, 6.0)

    def test_flashcard_extraction(self):
        md = "Note\nQ:: What is ACID? A:: Database guarantees.\n"
        cards = extract_flashcards_from_markdown(md, "node1")
        self.assertEqual(len(cards), 1)
        self.assertIn("ACID", cards[0].question)

if __name__ == "__main__":
    unittest.main()
