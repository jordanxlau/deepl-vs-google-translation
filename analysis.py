import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tqdm import tqdm
import sys
from levenshtein import levenshtein_fast, levenshtein

sentences = pd.read_csv("sentences.csv")
deepl_sentences = sentences.iloc[:,1]
google_sentences = sentences.iloc[:,2]

#all distances measured between deepl's translation and google's translation

#this array keeps track of how much the two softwares differ
distances = np.array([levenshtein(deepl_sentences[0],google_sentences[0])])

#this array keeps the average number of words
total_words = (len(deepl_sentences[0].split(" ")) + len(google_sentences[0].split(" ")))/2

# distances = np.vectorize(levenshtein)(deepl_sentences, google_sentences)

#compare the rest of the text
for i in tqdm (range(1, len(deepl_sentences)), colour="green", desc="Comparing Sentences...", file=sys.stdout):
    try:
        distances = np.append(distances, levenshtein(deepl_sentences[i],google_sentences[i]))
        total_words = np.append(total_words, (len(deepl_sentences[i].split(" ")) + len(google_sentences[i].split(" ")))/2)
    except Exception as e:
        pass

# computing statistical results
print("Average Levenshtein distance between Google translate and DeepL:", np.mean(distances))
print("Average Levenshtein distance per word:", np.mean(distances/total_words))

# Plot a comparison of deepl and google
plt.title("Comparison of DeepL and Google")
plt.plot(distances, color=(0,0.7,0.7))
plt.ylabel("distance")
plt.show()