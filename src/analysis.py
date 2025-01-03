import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from metrics import levenshtein
from tqdm import tqdm
import sys

def preprocess(s):
    return s.lower().replace(".","").replace("?","").replace("!","").replace(",","").replace(":","").replace(";","").replace("  "," ")

# read the data from the array
paragraphs = pd.read_csv("../data/paragraphs.csv")
english_paragraphs = paragraphs.iloc[:,0]
deepl_paragraphs = paragraphs.iloc[:,1]
google_paragraphs = paragraphs.iloc[:,2]
human_paragraphs = paragraphs.iloc[:,3]

# initialize arrays to keep track of how much the softwares differ
deepl_distances = np.array([])
google_distances = np.array([])
distances = np.array([])
num_words = np.array([])

#compare the rest of the text
for i in tqdm (range(0, len(english_paragraphs)), colour="green", desc="Comparing Paragraphs...", file=sys.stdout):
    # Preprocess the paragraph
    human = preprocess(human_paragraphs[i])
    deepl = preprocess(deepl_paragraphs[i])
    google = preprocess(google_paragraphs[i])
    english = preprocess(english_paragraphs[i])

    # Calculate and save the levenshtein distances
    try:
        deepl_distances = np.append(deepl_distances, levenshtein(deepl, human))
        google_distances = np.append(google_distances, levenshtein(google, human))
        distances = np.append(distances, levenshtein(google, deepl))
        num_words = np.append(num_words, len(english.split(" ")))
    except Exception as e:
        pass

# computing statistical results
print("Average Levenshtein distance between Google Translate and the Human Translation:", np.mean(google_distances))
print("Average Levenshtein distance between DeepL and the Human Translation:", np.mean(deepl_distances))
print("Average Levenshtein distance between DeepL and Google Translate:", np.mean(distances))
print("Per-English-Word Levenshtein distance between DeepL and the Human Translation:", np.mean(deepl_distances/num_words))
print("Per-English-Word Levenshtein distance between Google Translate and the Human Translation:", np.mean(google_distances/num_words))

# Plot a comparison of deepl and google
plt.title("Comparison of DeepL and Google Translation")
plt.plot(deepl_distances, label="DeepL", color="blue")
plt.plot(google_distances, label="Google", color="cyan")
plt.ylabel("levenshtein distance")
plt.legend()
plt.show()