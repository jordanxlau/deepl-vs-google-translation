import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from metrics import levenshtein, meteor
from tqdm import tqdm
import sys
import math

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
deepl_meteor = np.array([])
google_meteor = np.array([])
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

        # An issue is caused when encoding apostrophes from the Original French
        # This issue will be solved later
        x = meteor(deepl,human)
        y = meteor(google,human)
        if (math.isnan(x) or math.isnan(y)):
            continue
        deepl_meteor = np.append(deepl_meteor, meteor(deepl, human))
        google_meteor = np.append(google_meteor, meteor(google, human))
        
    except Exception as e:
        pass

# Plotting results

# Plot a comparison of deepl and google by levenshtein distance
plt.title("Comparison of DeepL and Google Translation")
plt.plot(deepl_distances, label="DeepL", color="blue")
plt.plot(google_distances, label="Google", color="cyan")
plt.ylabel("levenshtein distance")
plt.xlabel(
    "Average Levenshtein distance between Google Translate and the Human Translation:"
    + str(np.mean(google_distances))
    + "\nAverage Levenshtein distance between DeepL and the Human Translation:"
    + str(np.mean(deepl_distances))
    + "\nAverage Levenshtein distance between DeepL and Google Translate"
    + str(np.mean(distances))
    + "\nPer-English-Word Levenshtein distance between DeepL and the Human Translation:"
    + str(np.mean(deepl_distances/num_words))
    + "\nPer-English-Word Levenshtein distance between Google Translate and the Human Translation:"
    + str(np.mean(google_distances/num_words)),
    fontsize=10
)
plt.legend()
plt.show()

# Plot a comparison of deepl and google by METEOR
plt.title("Comparison of DeepL and Google Translation")
plt.plot(deepl_meteor, label="DeepL", color="blue")
plt.plot(google_meteor, label="Google", color="cyan")
plt.ylabel("modified meteor score")
plt.xlabel(
    "Average modified METEOR score between Google Translate and the Human Translation:"
    + str(np.mean(google_meteor))
    + "\nAverage modified METEOR score between DeepL and the Human Translation:"
    + str(np.mean(deepl_meteor)),
    fontsize=10
)
plt.legend()
plt.show()