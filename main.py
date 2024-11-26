from numpy import array, append, mean
from levenshtein import levenshtein
from translate import deepl_translate
from translate import google_translate
from tqdm import tqdm
import sys

#all distances measured between deepl's translation and google's translation

#prepares the text first
english_text = open('full-text.txt').read()
english_text = english_text.replace("\n", " ")
english_text = english_text.replace("â€™","'")
english_text = english_text.replace("Ã©","é")
english_text = english_text.lower()
english_sentences = english_text.split(".")

# fill the arrays with the first translated sentences
deepl_sentences = array([deepl_translate(english_sentences[0])])
google_sentences = array([google_translate(english_sentences[0])])

#this array keeps track of how much the two softwares differ
distances = array([levenshtein(deepl_sentences[0],google_sentences[0])])

#this array keeps the average number of words
total_words = (len(deepl_sentences[0].split(" ")) + len(google_sentences[0].split(" ")))/2

#translate the rest of the text and update the arrays
for i in tqdm (range(1, len(english_sentences)), desc="Translating...", file=sys.stdout):
    deepl_sentences = append(deepl_sentences, deepl_translate(english_sentences[i]))
    google_sentences = append(google_sentences, google_translate(english_sentences[i]))
    distances = append(distances, levenshtein(deepl_sentences[i],google_sentences[i]))
    total_words = append(total_words, (len(deepl_sentences[i].split(" ")) + len(google_sentences[i].split(" ")))/2)

#performing the statistical analysis here
print("Average Levenshtein distance between Google translate and DeepL:", mean(distances))
print("Average Levenshtein distance per word:", mean(distances/total_words))