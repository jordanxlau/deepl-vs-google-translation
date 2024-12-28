import ctypes
import os

def levenshtein(s,t):
    # Load the DLL
    lev_dll = ctypes.WinDLL(os.path.dirname(__file__) + "\\levenshtein.dll")

    # Call the function from the DLL
    return lev_dll.levenshtein(s.encode('utf-8'), t.encode('utf-8'))

def sentiment(s):
    from transformers import pipeline

    classifier = pipeline("sentiment-analysis")

    sentiment = classifier(s)
    if sentiment[0]['label'] == 'POSITIVE':
        return sentiment[0]['score']
    else:
        return -1*sentiment[0]['score']