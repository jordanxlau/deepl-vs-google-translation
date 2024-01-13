#the downside of this will be that context from other sentences is not kept
def sentence_translate():
    pass

import deepl
def deepl_translate(text):
    auth_key = open("/Users/jorda/Documents/deepl_auth_key.txt").read()
    translator = deepl.Translator(auth_key) 
    translation = translator.translate_text(text, target_lang="fr") 
    return translation.text

import googletrans as google
def google_translate(text):
    translator = google.Translator()
    translation = translator.translate(text, src = 'en', dest = 'fr')
    return translation.text
