#include <vector>
#include <string>
#include <iostream>
#include <cstddef>
#include <limits>
using namespace std;

// Method to convert a sentence String to a vector of words
static vector<string> vectorize(const char* s){
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

// Method to convert a list of tokens to a vector of tokens
static vector<int> vectorize(int s[], int len){
    vector<int> res = {}; // List of Strings
    int token;

    for (int i = 0; i<len; i++){
        token = s[i];
        res.push_back(token);
    }
    
    return res;
}

// Calculates the set intersection
template <typename T>
vector<T> intersection(vector<T> a, vector<T> b){
    vector<T> result = {};
    for (T worda : a){
        for (T& wordb : b){
            if (worda == wordb){
                result.push_back(worda);
                wordb = -1;
            }
        }
    }

    return result;
}

template <typename T>
double harmonic_mean(vector<T> ref_vector, vector<T> cand_vector){
    // Words in both the candidate translation and reference translation
    double m = intersection(ref_vector, cand_vector).size();
    // Number of words in the candidate translation
    double wt = cand_vector.size();
    // Number of words in the reference translation
    double wr = ref_vector.size();

    // Calculate 
    double recall = m/wr;
    double precision = m/wt;

    // Calculates the weighted harmonic mean
    return (10*precision*recall)/(recall+9*precision);
}

// Accepts a string of words
extern "C" __declspec(dllexport) double meteor(const char* reference, const char* candidate){
    vector<string> cand_vector = vectorize(candidate);
    vector<string> ref_vector = vectorize(reference);

    return harmonic_mean(ref_vector, cand_vector);
}

// Accepts an array of tokens
extern "C" __declspec(dllexport) double meteor_tokenized(int reference[], int candidate[], int ref_len, int cand_len){
    vector<int> cand_vector = vectorize(candidate, cand_len);
    vector<int> ref_vector = vectorize(reference, ref_len);

    return harmonic_mean(ref_vector, cand_vector);
}