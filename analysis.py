import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from levenshtein import levenshtein
from tqdm import tqdm
import sys

paragraphs = pd.read_csv("paragraphs.csv")
deepl_paragraphs = paragraphs.iloc[:,1]
google_paragraphs = paragraphs.iloc[:,2]
human_translated_paragraphs = paragraphs.iloc[:,3]

# distances measured between (deepl's translation or google's translation) and the human translation

#this array keeps track of how much the two softwares differ
deepl_distances = np.array([])
google_distances = np.array([])


# deepl_distances = np.vectorize(levenshtein)(deepl_sentences, human_translated_sentences)
# google_distances = np.vectorize(levenshtein)(deepl_sentences, human_translated_sentences)

#compare the rest of the text
for i in tqdm (range(0, len(deepl_paragraphs)), colour="green", desc="Comparing Paragraphs...", file=sys.stdout):
    try:
        deepl_distances = np.append(deepl_distances, levenshtein(deepl_paragraphs[i],human_translated_paragraphs[i]))
        google_distances = np.append(google_distances, levenshtein(google_paragraphs[i],human_translated_paragraphs[i]))
    except Exception as e:
        pass

# computing statistical results
print("Average Levenshtein distance between Google Translate and the Human Translation:", np.mean(google_distances))
print("Average Levenshtein distance between DeepL and the Human Translation:", np.mean(deepl_distances))

# Plot a comparison of deepl and google
plt.title("Comparison of DeepL and Google Translation")
plt.plot(deepl_distances, label="DeepL", color="blue")
plt.plot(google_distances, label="Google", color="cyan")
plt.ylabel("levenshtein distance")
plt.legend()
plt.show()