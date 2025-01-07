import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from metrics import lev_tokenized, meteor_tokenized
from tqdm import tqdm
import sys
import math

def preprocess(s):
    return s.lower().replace(".","").replace("’","'").replace("?","").replace("!","").replace(",","").replace(":","").replace(";","").replace("  "," ")

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
deepl_meteor = np.array([])
google_meteor = np.array([])
scores = np.array([])
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
        deepl_distances = np.append(deepl_distances, lev_tokenized(deepl, human))
        google_distances = np.append(google_distances, lev_tokenized(google, human))
        distances = np.append(distances, lev_tokenized(google, deepl))
        num_words = np.append(num_words, len(english.split(" ")))

        deepl_current_score = meteor_tokenized(deepl, human)
        google_current_score  = meteor_tokenized(google, human)
        current_score = meteor_tokenized(google, deepl)
        if(not math.isnan(deepl_current_score) and not math.isnan(google_current_score) and not math.isnan(current_score)):
            deepl_meteor = np.append(deepl_meteor, deepl_current_score)
            google_meteor = np.append(google_meteor, google_current_score)
            scores = np.append(scores, current_score)    
    except Exception as e:
        pass

# Plotting results

# Plot a comparison of deepl and google by levenshtein distance
plt.title("Comparison of DeepL and Google Translation")
plt.plot(deepl_distances/num_words, label="DeepL", color="blue")
plt.plot(google_distances/num_words, label="Google", color="cyan")
plt.ylabel("Levenshtein distance (per English word)")
plt.xlabel(
    "Mean distance between DeepL and Google Translate"
    + str(np.mean(distances/num_words))
    + "\nMean distance between DeepL and reference Translation:"
    + str(np.mean(deepl_distances/num_words))
    + "\nMean distance between Google Translate and reference Translation:"
    + str(np.mean(google_distances/num_words)),
    fontsize=9
)
plt.legend()
plt.show()

# Plot a comparison of deepl and google by METEOR
plt.title("Comparison of DeepL and Google Translation")
plt.plot(deepl_meteor, label="DeepL", color="blue")
plt.plot(google_meteor, label="Google", color="cyan")
plt.ylabel("Modified METEOR score")
plt.xlabel(
    "Mean score between DeepL and Google Translate: "
    + str(np.mean(scores))
    + "\nMean score between Google Translate and reference Translation: "
    + str(np.mean(google_meteor))
    + "\nMean score between between DeepL and reference Translation:"
    + str(np.mean(deepl_meteor)),
    fontsize=9
)
plt.legend()
plt.show()