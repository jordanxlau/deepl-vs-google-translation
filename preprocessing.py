from translate import deepl_translate
from translate import google_translate
from tqdm import tqdm
import sys
import pandas as pd

# preprocess the English text
english_text = open('full-text.txt', encoding="utf-8").read()
english_text = english_text.replace("\n\n", "§") # define paragraphs
english_text = english_text.lower()
english_text = english_text.replace('"','')

# split the text by paragraphs
english_paragraphs = english_text.split("§")

# preprocess french text
french_text = open('full-text-fr.txt', encoding="utf-8").read()
french_text = french_text.replace("\n\n", "§") # define paragraphs
french_text = french_text.lower()
french_text = french_text.replace('"','')
french_text = french_text.replace('«','')
french_text = french_text.replace('»','')
french_text = french_text.replace('--',' ')

# split the text by paragraphs
human_translated_paragraphs = french_text.split("§")

# initializing the arrays
deepl_paragraphs = []
google_paragraphs = []

# translate the text
for i in tqdm (range(0, len(english_paragraphs)), colour="green", desc="Translating...", file=sys.stdout):
    deepl_paragraphs.append(deepl_translate(english_paragraphs[i]))
    google_paragraphs.append(google_translate(english_paragraphs[i]))

# save the data as a .csv
paragraphs = pd.DataFrame({
    "original english paragraphs":english_paragraphs,
    "deepl paragraphs":deepl_paragraphs,
    "google paragraphs":google_paragraphs,
    "human-translated paragraphs":human_translated_paragraphs
})
paragraphs.to_csv("paragraphs.csv", encoding='utf-8', index=False)