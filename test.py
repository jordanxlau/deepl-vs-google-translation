import unittest
from levenshtein import levenshtein
from translate import deepl_translate, google_translate

class TestLev(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual(levenshtein("hello jordan","hello meghan"), 1)
        self.assertEqual(levenshtein("he is","she is"), 1)
        self.assertEqual(levenshtein("War of the Worlds","For of the Worlds"), 1)
        self.assertEqual(levenshtein("Two","Two hundered"), 1)
        self.assertEqual(levenshtein("Seventeen different people","different"), 2)
        self.assertEqual(levenshtein("Ten terrible tantrums on Tuesday","Five feverish fits on Friday"), 4)
        self.assertEqual(levenshtein("Salut, je m'appelle Jordan","Bonjour, je m'appelle Jordan"), 1)
    
    def test_two(self):
        self.assertEqual(levenshtein("était","etait"),1)
        self.assertEqual(levenshtein("il s'appelle","il se appelle"),2)
        self.assertEqual(levenshtein("il s'appelle","il appelle"),1)

class TestTranslate(unittest.TestCase):
    def test_deepl(self):
        self.assertEqual(deepl_translate("Hello"),"Bonjour")
        self.assertEqual(deepl_translate("Yes"),"Oui")

    def test_google(self):
        self.assertEqual(google_translate("Hello"),"Bonjour")
        self.assertEqual(deepl_translate("Yes"),"Oui")

if __name__ == '__main__':
    unittest.main()