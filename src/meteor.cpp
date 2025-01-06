#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <iostream>
using namespace std;

// Method to convert a sentence String to a list/vector of words
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

vector<string> intersection(vector<string> a, vector<string> b){
    vector<string> result = {};
    for (string worda : a){
        for (string& wordb : b){
            if (worda == wordb){
                result.push_back(worda);
                wordb = "";
            }
        }
    }
    return result;
}

double harmonic_mean(vector<string> ref_vector, vector<string> cand_vector){
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

// Accepts a list of tokens
extern "C" __declspec(dllexport) double meteor(const char* reference, const char* candidate){
    vector<string> cand_vector = vectorize(candidate);
    vector<string> ref_vector = vectorize(reference);
    
    return harmonic_mean(ref_vector, cand_vector);
}