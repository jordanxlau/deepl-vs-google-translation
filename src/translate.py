#provides functions that use deepl and googletranslate packages to translate text
import os
import deepl
import googletrans as google

def deepl_translate(text):
    if text == "":
        return ""
    auth_key = open(os.path.dirname(__file__) + "\\deepl_auth_key.txt").read()
    translator = deepl.Translator(auth_key) 
    translation = translator.translate_text(text, target_lang="fr") 
    return translation.text

def google_translate(text):
    if text == "":
        return ""
    translator = google.Translator()
    translation = translator.translate(text, src = 'en', dest = 'fr')
    return translation.text
