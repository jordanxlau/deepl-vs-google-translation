import unittest
from src.metrics import levenshtein, meteor, lev_tokenized, meteor_tokenized, sentiment

class TestCases(unittest.TestCase):
    def test_lev(self):
        self.assertEqual(levenshtein("levenshtein distance","levenshtein distance"), 0)
        self.assertEqual(levenshtein("hello jordan","hello meghan"), 1)
        self.assertEqual(levenshtein("he is","she is"), 1)
        self.assertEqual(levenshtein("two","two hundered"), 1)
        self.assertEqual(levenshtein("la guerre des mondes","le paire des mondes"), 2)
        self.assertEqual(levenshtein("ten terrible tantrums on tuesday","five feverish fits on friday"), 4)
        self.assertEqual(levenshtein("était","etait"),1)
        self.assertEqual(levenshtein("il s'appelle","il se appelle"),2)
        self.assertEqual(levenshtein("il s'appelle","il appelle"),1)
        self.assertEqual(levenshtein("ce sont les traductions","les traductions sont là"), 4)
        self.assertEqual(levenshtein("j'ai 585", "j'en ai 585"), 2)

    def test_lev_tokenized(self):
        self.assertEqual(lev_tokenized("antidisestablishmentarianism","antidisestablishmentarianism"),0)
        self.assertEqual(lev_tokenized("the cat","the mouse"), 1)
        self.assertEqual(lev_tokenized("il s'appelle","il m'appelle"),1)
        self.assertEqual(lev_tokenized("j'ai 585", "j'en ai 585"), 1)
        self.assertEqual(lev_tokenized("antidisestablishmentarianism", ""), 8)

    def test_meteor(self):
        self.assertEqual(meteor("the cat sat on the mat","on the mat sat the cat"), 1)
        self.assertEqual(meteor("the cat sat on the mat","the cat sat on the mat"), 1)
        self.assertAlmostEqual(meteor("the cat sat on the mat","the cat was sat on the mat"), 0.9836, places=4)
        self.assertEqual(meteor("le chat est sur le tapis","le chat est sur le tapis"), 1)
        self.assertAlmostEqual(meteor("le chat est sur le tapis","le chat il est sur le tapis"), 0.9836, places=4)

    def test_meteor_tokenized(self):
        self.assertEqual(meteor_tokenized("the cat sat on the mat","on the mat sat the cat"), 1)
        self.assertAlmostEqual(meteor_tokenized("the kit sat on the mat","the kitty sat on the mat"), 0.9836, places=4)

    def test_sentiment(self):
        self.assertGreater(sentiment("I love you!"), 0.98)
        self.assertLess(sentiment("This sucks!"), -0.98)

if __name__ == '__main__':
    unittest.main()