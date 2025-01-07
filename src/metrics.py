import ctypes
import os

# Load the DLLs
meteor_dll = ctypes.CDLL(os.path.dirname(__file__) + "\\meteor.dll")
lev_dll = ctypes.WinDLL(os.path.dirname(__file__) + "\\levenshtein.dll")

# Set arg types
meteor_dll.meteor_tokenized.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]

# Set resolution types
meteor_dll.meteor.restype = ctypes.c_double
meteor_dll.meteor_tokenized.restype = ctypes.c_double

def levenshtein(s,t):
    # Call the levenshtein distance function from the DLL
    return lev_dll.levenshtein(s.encode('utf-8'), t.encode('utf-8'))

def meteor(s,t):
    # Call the meteor function from the DLL
    return meteor_dll.meteor(s.encode('utf-8'), t.encode('utf-8'))

def meteor_tokenized(s,t):
    from transformers import BertTokenizer
    # initialize a tokenizer
    bert = BertTokenizer.from_pretrained("bert-base-cased")
    s = bert.tokenize(s)
    t = bert.tokenize(t)
    s = bert.convert_tokens_to_ids(s)
    t = bert.convert_tokens_to_ids(t)

    print(s,t)

    # Call the meteor function from the DLL
    return meteor_dll.meteor_tokenized((ctypes.c_int * len(s))(*s),(ctypes.c_int * len(t))(*t), len(s), len(t))

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