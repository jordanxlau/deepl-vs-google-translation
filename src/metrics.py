import ctypes
import os

def levenshtein(s,t):
    # Load the DLL
    lev_dll = ctypes.WinDLL(os.path.dirname(__file__) + "\\levenshtein.dll")

    # Call the levenshtein distance function from the DLL
    return lev_dll.levenshtein(s.encode('utf-8'), t.encode('utf-8'))

def meteor(s,t):
    # Load the DLL
    meteor_dll = ctypes.CDLL(os.path.dirname(__file__) + "\\meteor.dll")
    
    # Set resolution type to double
    meteor_dll.meteor.restype = ctypes.c_double

    # Call the meteor function from the DLL
    return meteor_dll.meteor(s.encode('utf-8'), t.encode('utf-8'))

def sentiment(s):
    # Import transformers library within the function to avoid unecessarily performing the import
    # This import is very slow and should not be run unless sentiment() will be called
    from transformers import pipeline

    # Create a classifier
    classifier = pipeline("sentiment-analysis")

    # Classify the sentence
    sentiment = classifier(s)

    # Sentiment is returned as a negative value if it is considered negative
    # Thus, the range of possible returns
    if sentiment[0]['label'] == 'POSITIVE':
        return sentiment[0]['score']
    else:
        return -1*sentiment[0]['score']