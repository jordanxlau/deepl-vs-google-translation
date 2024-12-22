from translate import deepl_translate
from translate import google_translate
from tqdm import tqdm
import sys
import pandas as pd


#prepares the text first
english_text = open('full-text.txt').read()
english_text = english_text.replace("\n", " ")
english_text = english_text.replace("â€™","'")
english_text = english_text.replace("Ã©","é")
english_text = english_text.lower()
english_sentences = english_text.split(".")

# fill the arrays with the first translated sentences
deepl_sentences = [deepl_translate(english_sentences[0])]
google_sentences = [google_translate(english_sentences[0])]


#translate the rest of the text
for i in tqdm (range(1, len(english_sentences)), colour="green", desc="Translating...", file=sys.stdout):
    deepl_sentences.append(deepl_translate(english_sentences[i]))
    google_sentences.append(google_translate(english_sentences[i]))


# Save the data
sentences = pd.DataFrame({
    "original english sentences":english_sentences,
    "deepl sentences":deepl_sentences,
    "google sentences":google_sentences
})
sentences.to_csv("sentences.csv", index=False)