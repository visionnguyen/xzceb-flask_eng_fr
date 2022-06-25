import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(''),'')
        self.assertNotEqual(english_to_french('Hello'),'Hello')
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(''),'')
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour)
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()
