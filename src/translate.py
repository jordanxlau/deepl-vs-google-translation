# Provides functions that use the DeepL API and googletrans package to translate text
import os
import deepl
from googletrans import Translator

def deepl_translate(text):
    if text == "":
        return ""
    auth_key = open(os.path.dirname(__file__) + "\\deepl_auth_key.txt").read()
    translator = deepl.Translator(auth_key) 
    translation = translator.translate_text(text, target_lang="fr") 
    return translation.text

async def google_translate(text):
    async with Translator() as translator:
        result = await translator.translate(text, src='en', dest='fr')
        return result.text
