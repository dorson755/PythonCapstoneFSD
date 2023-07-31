"""Translator Module"""

from deep_translator import GoogleTranslator

def english_to_french(text):
    '''English to French'''
    #Receives text in English and returns its French translation.
    my_translator = GoogleTranslator(source='auto', target='german')
    result = my_translator.translate(text=text)
    return result


def english_to_german(text):
    """English to German"""
    #Receives text in English and returns its German translation.
    my_translator = GoogleTranslator(source='auto', target='french')
    result = my_translator.translate(text=text)
    return result
    