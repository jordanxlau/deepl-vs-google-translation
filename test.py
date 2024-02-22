import unittest
from levenshtein import levenshtein

class TestLev(unittest.TestCase):

    def test_one(self):
        self.assertEqual(levenshtein("jordan","jordan"), 0)
        self.assertEqual(levenshtein("hat","cat"), 1)
        self.assertEqual(levenshtein("kitten","sitting"), 3)
        self.assertEqual(levenshtein("Saturday","Sunday"), 3)
        self.assertEqual(levenshtein("Salut, je m'appelle Jordan","Bonjour, je m'appelle Jordan"), 6)
    
    def test_two(self):
        self.assertEqual(levenshtein("Jordan","jordan"),0)
        self.assertEqual(levenshtein("était","etait"),1)

if __name__ == '__main__':
    unittest.main()