import unittest
import sys
sys.path.append("machinetranslation")
import translator
from translator import french_to_english, english_to_french


class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french("None"), '')
    
    def test_english_to_german(self):
        self.assertEqual(english_to_german('Hello'), 'Hallo')
        self.assertNotEqual(english_to_german("None"), '')

if __name__ == '__main__':
    unittest.main()