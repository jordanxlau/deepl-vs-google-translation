from numpy import array, append
from time import sleep

from levenshtein import levenshtein
from translate import deepl_translate
from translate import google_translate

#all distances measured between deepl's translation and google's translation

#prepares the text first
english_text = open('original-english.txt').read()
english_text = english_text.replace("\n", " ")
english_text = english_text.replace("â€™","'")
english_text = english_text.replace("Ã©","é")
english_text = english_text.lower()
english_sentences = english_text.split(".")

# fill the arrays with the first translated sentences
deepl_sentences = array([deepl_translate(english_sentences[0])])
google_sentences = array([google_translate(english_sentences[0])])

#this array keeps track of how much the two softwares differ
print(deepl_sentences[0])
print("\n")
print(google_sentences[0])
print(levenshtein(deepl_sentences[0],google_sentences[0]))
distances = array([levenshtein(deepl_sentences[0],google_sentences[0])])

#translate the rest of the array
# for i in range(1, len(english_sentences)):
#     print(i)
#     append(deepl_sentences, deepl_translate(english_sentences[i]))
#     append(google_sentences, google_translate(english_sentences[i]))
#     print(levenshtein(deepl_sentences[i],google_sentences[i]))
#     append(distances, levenshtein(deepl_sentences[i],google_sentences[i]))

# print(deepl_sentences)
# print(google_sentences)