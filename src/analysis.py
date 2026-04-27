import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from tqdm import tqdm

from metrics import levenshtein, meteor

import sys
import math

def preprocess(s):
    return s.lower().replace(".","").replace("’","'").replace("?","").replace("!","").replace(",","").replace(":","").replace(";","").replace("  "," ")

# read the data from the array
sentences = pd.read_csv("../data/sentences.csv")
english_sentences = sentences.iloc[:,0]
deepl_sentences = sentences.iloc[:,1]
google_sentences = sentences.iloc[:,2]
human_sentences = sentences.iloc[:,3]

# initialize arrays to keep track of how much the softwares differ
deepl_distances = np.array([])
google_distances = np.array([])
distances = np.array([])
deepl_meteor = np.array([])
google_meteor = np.array([])
scores = np.array([])
num_words = np.array([])

# Compare the text
for i in tqdm (range(0, len(english_sentences)), colour="green", desc="Comparing sentences...", file=sys.stdout):
    # Preprocess the paragraph
    human = preprocess(human_sentences[i])
    deepl = preprocess(deepl_sentences[i])
    google = preprocess(google_sentences[i])
    english = preprocess(english_sentences[i])

    # Calculate and save the levenshtein distances
    try:
        deepl_distances = np.append(deepl_distances, levenshtein(deepl, human))
        google_distances = np.append(google_distances, levenshtein(google, human))
        distances = np.append(distances, levenshtein(google, deepl))
        num_words = np.append(num_words, len(english.split(" ")))

        deepl_current_score = meteor(deepl, human)
        google_current_score  = meteor(google, human)
        current_score = meteor(google, deepl)
        if(not math.isnan(deepl_current_score) and not math.isnan(google_current_score) and not math.isnan(current_score)):
            deepl_meteor = np.append(deepl_meteor, deepl_current_score)
            google_meteor = np.append(google_meteor, google_current_score)
            scores = np.append(scores, current_score)    
    except Exception as e:
        pass

# Create heatmaps for results
lev_map = np.array(
    [   # DeepL, Google, Reference
        [0, np.mean(distances/num_words), np.mean(deepl_distances/num_words)], # DeepL
        [None, 0, np.mean(google_distances/num_words)], # Google
        [None, None, 0], # Reference
    ],
    dtype=float,
)

meteor_map = np.array(
    [   # DeepL, Google, Reference
        [1, np.mean(scores), np.mean(deepl_meteor)], # DeepL
        [None, 1, np.mean(google_meteor)], # Google
        [None, None, 1], # Reference
    ],
    dtype=float,
)

# Plotting results
sns.heatmap(
    lev_map,
    annot=True,
    xticklabels=["DeepL","Google","Reference"],
    yticklabels=["DeepL","Google","Reference"],
    cmap=sns.color_palette("crest_r", as_cmap=True)
)
plt.title("Mean Levenshtein Distance (per English word)")
plt.show()

sns.heatmap(
    meteor_map,
    annot=True,
    xticklabels=["DeepL","Google","Reference"],
    yticklabels=["DeepL","Google","Reference"],
    cmap=sns.color_palette("crest", as_cmap=True)
)
plt.title("Mean (modified) METEOR score")
plt.show()