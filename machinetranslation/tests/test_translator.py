"""
Module Name: test_translator.py
Description: This is the test module for translator.py.

Author: Dorson Williams
Date: August 2023
"""

import unittest
#import sys
from machinetranslation.translator import english_to_german, english_to_french
#sys.path.append("machinetranslation")


class TestTranslator(unittest.TestCase):
    '''class for unit test'''
def test_english_to_french(self):
    '''en to fr'''
    self.assertEqual(english_to_french('Hello'), 'Bonjour')
    #self.assertNotEqual(english_to_french("None"), '')

def test_english_to_german(self):
    '''en to de'''
    self.assertEqual(english_to_german('Hello'), 'Hallo')
    #self.assertNotEqual(english_to_german("None"), '')

if __name__ == '__main__':
    unittest.main()
