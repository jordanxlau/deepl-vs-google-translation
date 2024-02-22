from numpy import zeros

# to be called on two nonzero sentences
# this implementation measures the lev distance by word, not by character
# ie. levenshtein("hello jordan","hello meghan") = 1
def levenshtein(s,t):
    #convert the sentences of words to lists of words
    s = s.split(" ")
    t = t.split(" ")

    #add a blank character to the end of all the words, as this version of lev distance cannot account for last characters
    s.append("finalword")
    t.append("finalword")

    #get the length of the words
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
            d[i, j] = min(
                    d[i-1, j] + 1,                     # deletion
                    d[i, j-1] + 1,                     # insertion
                    d[i-1, j-1] + substitutionCost)    # substitution
            
    return d[m-1, n-1]