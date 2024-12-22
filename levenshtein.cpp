// from numpy import zeros
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

// Method to take minimum of 3 integers
static int min(int i, int j, int k){
    if (i <= j && i <= k)
        return i;
    else if (j <= k && j <= i)
        return j;
    else
        return k;
}

// Method to split a String by " "
static vector<string> split(const char* s){
    vector<string> res = {}; // List of Strings
    string word = "";

    for (int i = 0; i<strlen(s); i++){
        if (s[i] != ' ') {
            word = word + s[i];
        }
        else if (s[i] == ' '){
            res.push_back(word);
            word = "";
        }
    }
    
    res.push_back(word);
  
    return res;
}

// to be called on two nonzero sentences
// this implementation measures the lev distance by word, not by character
// ie. levenshtein("hello jordan","hello meghan") = 1
extern "C" __declspec(dllexport) int levenshtein(const char* arg1, const char* arg2) {
    //convert the sentences of words to lists of words
    vector<string> s = split(arg1);
    vector<string> t = split(arg2);
    
    //add a blank character to the end of all the words, as this version of lev distance cannot account for last characters
    s.push_back("finalword");
    t.push_back("finalword");

    //get the length of the words
    int m = s.size();
    int n = t.size();

    // for all i and j, d[i][j] will hold the Levenshtein distance between
    // the first i characters of s and the first j characters of t
    
    //create a matrix of zeros of length mxn
    vector<vector<int>> d;
    for (int i = 0; i < m; i++){
        vector<int> row;
        for (int j = 0; j<n; j++){
            row.push_back(0);
        }
        d.push_back(row);
        row = {};
    }

    // source prefixes can be transformed into empty string by
    // dropping all characters
    for (int i = 1; i<m; i++)
        d[i][0] = i;

    // target prefixes can be reached from empty source prefix
    // by inserting every character
    for (int j = 0; j<n; j++)
        d[0][j] = j;
    
    int substitutionCost = 1;

    for (int j = 1; j<n; j++){
        for (int i = 1; i<m; i++){
            if (s[i-1] == t[j-1])//I think wikipedia was wrong about this line
                substitutionCost = 0;
            else
                substitutionCost = 1;
            d[i][j] = min(
                    d[i-1][j] + 1,                     // deletion
                    d[i][j-1] + 1,                     // insertion
                    d[i-1][j-1] + substitutionCost);    // substitution
        }
    }

    return d[m-1][n-1];
}