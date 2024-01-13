from numpy import array
import pandas as pd
from translate import deepl_translate
from translate import google_translate

#to be called on two sentences of nonzero length
def lev(a,b):
    if(len(a)==0):
        return len(b)
    elif(len(b)==0):
        return len(a)
    elif(a[0]==b[0]):
        return lev(a[1:], b[1:])
    else:
        return 1 + min(lev(a[1:],b), lev(a, b[1:]), lev(a[1:],b[1:]))

#all distances measured between machine translation and original translation
deepl_distance = array([])
google_distance = array([])

english_text = open('original-english.txt').read()
english_text = english_text.replace("\n", " ")
english_text = english_text.replace("â€™","'")
english_text = english_text.replace("Ã©","é")
english_sentences = english_text.split(".")

translated_text = open('french-translation.txt').read()
translated_text = translated_text.replace("\n", " ")
translated_text = translated_text.replace("â€™","'")
translated_text = translated_text.replace("Ã©","é")
translated_text = translated_text.replace("Ã¨","è")
translated_text = translated_text.replace("Ã\xa0","à")
translated_text = translated_text.replace("Ã§","ç")
translated_text = translated_text.replace("Ãª","ê")
translated_text = translated_text.replace("Ã»","û")
translated_text = translated_text.replace("Ã´","ô")
translated_sentences = translated_text.split(".")

print(translated_sentences)

for i in range(0, len(english_sentences)):
    deepl_distance[i] = lev(translated_sentences[i], deepl_translate(english_sentences[i]))
    google_distance[i] = lev(translated_sentences[i], google_translate(english_sentences[i]))
