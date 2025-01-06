import unittest
from src.metrics import levenshtein, meteor, sentiment
from src.translate import deepl_translate, google_translate

class TestCases(unittest.TestCase):
    def test_lev_english(self):
        self.assertEqual(levenshtein("levenshtein distance","levenshtein distance"), 0)
        self.assertEqual(levenshtein("hello jordan","hello meghan"), 1)
        self.assertEqual(levenshtein("he is","she is"), 1)
        self.assertEqual(levenshtein("war of the worlds","for of the worlds"), 1)
        self.assertEqual(levenshtein("two","two hundered"), 1)
        self.assertEqual(levenshtein("seventeen different people","different"), 2)
        self.assertEqual(levenshtein("ten terrible tantrums on tuesday","five feverish fits on friday"), 4)
    
    def test_lev_french(self):
        self.assertEqual(levenshtein("était","etait"),1)
        self.assertEqual(levenshtein("il s'appelle","il se appelle"),2)
        self.assertEqual(levenshtein("il s'appelle","il appelle"),1)
        self.assertEqual(levenshtein("Salut, je m'appelle Jordan","Bonjour, je m'appelle Jordan"), 1)
        self.assertEqual(levenshtein("ce sont les traductions","les traductions sont là"), 4)
        self.assertEqual(levenshtein("j'ai 585", "j'en ai 585"), 2)

    def test_meteor_english(self):
        self.assertEqual(round(meteor("the cat sat on the mat","on the mat sat the cat"), 4), 1)
        self.assertEqual(round(meteor("the cat sat on the mat","the cat sat on the mat"), 4), 1)
        self.assertEqual(round(meteor("the cat sat on the mat","the cat was sat on the mat"), 4), 0.9836)

    def test_meteor_french(self):
        self.assertEqual(round(meteor("le chat est sur le tapis","sur le tapis est le cat"), 4), 1)
        self.assertEqual(round(meteor("le chat est sur le tapis","le chat est sur le tapis"), 4), 1)
        self.assertEqual(round(meteor("le chat est sur le tapis","le chat il est sur le tapis"), 4), 0.9836)

    def test_sentiment(self):
        self.assertTrue(sentiment("I love you!") > 0.98)
        self.assertTrue(sentiment("This sucks!") < -0.98)

    def test_deepl(self):
        self.assertEqual(deepl_translate("Hello"),"Bonjour")
        self.assertEqual(deepl_translate("Yes"),"Oui")

    def test_google(self):
        self.assertEqual(google_translate("Hello"),"Bonjour")
        self.assertEqual(google_translate("Yes"),"Oui")

if __name__ == '__main__':
    unittest.main()