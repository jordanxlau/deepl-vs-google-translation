from tqdm import tqdm
from datasets import load_dataset
import pandas as pd
import asyncio

from translate import deepl_translate, google_translate

import sys

# Load the WMT-14 Test dataset from HuggingFace
ds = load_dataset("wmt/wmt14", "fr-en", split="test")

# Initialize arrays
original_sentences = []
deepl_sentences = []
google_sentences = []
human_sentences = []

lengths = 0

# Iterate through the dataset
for row in tqdm(ds["translation"], colour="green", desc="Translating...", file=sys.stdout):
    # Preprocess the text
    english_text = row["en"].replace('\n',' ').replace('"','')
    french_text = row["fr"].replace('"','').replace('«','').replace('»','').replace('\n',' ')

    # Save the text
    original_sentences.append( english_text )
    lengths+=len(english_text)
    deepl_sentences.append(deepl_translate(english_text))
    google_sentences.append(asyncio.run(google_translate(english_text)))
    human_sentences.append(french_text)

# Save the data as a .csv
sentences = pd.DataFrame({
    "English-Original": original_sentences,
    "DeepL-Translated": deepl_sentences,
    "Google-Translated": google_sentences,
    "Human-Translated": human_sentences
})

sentences.to_csv("../data/sentences.csv", encoding='utf-8', index=False)