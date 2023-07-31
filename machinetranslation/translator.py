import os
from deep_translator import GoogleTranslator

def english_to_french(text):
    #Receives text in English and returns its French translation.
    my_translator = GoogleTranslator(source='auto', target='german')
    result = my_translator.translate(text=text)
    print(f"Translation using source = {my_translator.source} and target = {my_translator.target} -> {result}")
    return result

def english_to_german(text):
    #Receives text in English and returns its German translation.
    my_translator = GoogleTranslator(source='auto', target='french')
    result = my_translator.translate(text=text)
    print(f"Translation using source = {my_translator.source} and target = {my_translator.target} -> {result}")
    return result