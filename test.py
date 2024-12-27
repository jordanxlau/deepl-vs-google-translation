import unittest
from src.metrics import levenshtein
from src.translate import deepl_translate, google_translate

class TestLev(unittest.TestCase):
    def test_one(self):
        self.assertEqual(levenshtein("levenshtein distance","levenshtein distance"), 0)
        self.assertEqual(levenshtein("hello jordan","hello meghan"), 1)
        self.assertEqual(levenshtein("he is","she is"), 1)
        self.assertEqual(levenshtein("war of the worlds","for of the worlds"), 1)
        self.assertEqual(levenshtein("two","two hundered"), 1)
        self.assertEqual(levenshtein("seventeen different people","different"), 2)
        self.assertEqual(levenshtein("ten terrible tantrums on tuesday","five feverish fits on friday"), 4)
    
    def test_two(self):
        self.assertEqual(levenshtein("était","etait"),1)
        self.assertEqual(levenshtein("il s'appelle","il se appelle"),2)
        self.assertEqual(levenshtein("il s'appelle","il appelle"),1)
        self.assertEqual(levenshtein("Salut, je m'appelle Jordan","Bonjour, je m'appelle Jordan"), 1)
        self.assertEqual(levenshtein("ce sont les traductions","les traductions sont là"), 4)
        self.assertEqual(levenshtein("j'ai 585", "j'en ai 585"), 2)

class TestTranslate(unittest.TestCase):
    def test_five(self):
        self.assertEqual(deepl_translate("Hello"),"Bonjour")
        self.assertEqual(deepl_translate("Yes"),"Oui")

    def test_six(self):
        self.assertEqual(google_translate("Hello"),"Bonjour")
        self.assertEqual(google_translate("Yes"),"Oui")

if __name__ == '__main__':
    unittest.main()