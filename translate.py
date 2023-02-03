def word_for_word_translate():
    pass

import deepl
def deepl_translate(text):
    auth_key = ""
    translator = deepl.Translator(auth_key) 
    return translator.translate_text(text, target_lang="french") 

import googletrans as google
def google_translate(text):
    text = "good morning, my name is Jordan"
    translator = google.Translator()
    translation = translator.translate(text, src = 'en', dest = 'fr')
    return translation.text
