from numpy import array, append, zeros
from time import sleep
# import pandas as pd
from translate import deepl_translate
from translate import google_translate

def levenshtein(s,t):
    m = len(s)
    n = len(t)

    # for all i and j, d[i,j] will hold the Levenshtein distance between
    # the first i characters of s and the first j characters of t
    
    #set each element in matrix d to zero
    d = zeros((m, n))
 
    # source prefixes can be transformed into empty string by
    # dropping all characters
    for i in range(1, m):
        d[i, 0] = i
 
    # target prefixes can be reached from empty source prefix
    # by inserting every character
    for j in range (1, n):
        d[0, j] = j
    
    substitutionCost = 1

    for j in range(1, n):
        for i in range(1, m):
            if s[i-1] == t[j-1]:#I think wikipedia was wrong about this line
                substitutionCost = 0
            else:
                substitutionCost = 1
            # print(i,j,s[i],t[j],substitutionCost)
            d[i, j] = min(
                    d[i-1, j] + 1,                     # deletion
                    d[i, j-1] + 1,                     # insertion
                    d[i-1, j-1] + substitutionCost)    # substitution
            # print(d[i-1, j] + 1,d[i, j-1] + 1,d[i-1, j-1] + substitutionCost)
    print(d)
    return d[m-1, n-1]

# #all distances measured between deepl's translation and google's translation

# #prepares the text first
# english_text = open('original-english.txt').read()
# english_text = english_text.replace("\n", " ")
# english_text = english_text.replace("â€™","'")
# english_text = english_text.replace("Ã©","é")
# english_sentences = english_text.split(".")

# english_sentences = ["Hello my name is Jordan"]

# # fill the arrays with the first translated sentences
# deepl_sentences = array([deepl_translate(english_sentences[0])])
# google_sentences = array([google_translate(english_sentences[0])])

# #this array keeps track of how much the two softwares differ
# print(deepl_sentences[0])
# print(google_sentences[0])
# print(lev(deepl_sentences[0],google_sentences[0]))
# distances = array([lev(deepl_sentences[0],google_sentences[0])])

# #translate the rest of the array
# for i in range(1, len(english_sentences)):
#     print(i)
#     append(deepl_sentences, deepl_translate(english_sentences[i]))
#     append(google_sentences, google_translate(english_sentences[i]))
#     print(lev(deepl_sentences[i],google_sentences[i]))
#     append(distances, lev(deepl_sentences[i],google_sentences[i]))

# # print(deepl_sentences)
# # print(google_sentences)