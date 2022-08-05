import unittest
from translator import *


class TestE2FTranslation(unittest.TestCase):
    def test_null_value(self):
        self.assertEqual(english_to_french(None), "You need to send an input")

    
    def test_valid_arguement(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestF2ETranslation(unittest.TestCase):
    def test_null_value(self):
        self.assertEqual(french_to_english(None), "You need to send an input")
    
    def test_valid_arguement(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
