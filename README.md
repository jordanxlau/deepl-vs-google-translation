This study is a personal project that compares Google’s Neural Machine Translation with DeepL, a small German startup claiming to have outdone the tech giant in terms of the accuracy of its machine translation software.
The main metric used is levenshtein distance. I implement the dynamic programming version from:
https://en.wikipedia.org/wiki/Levenshtein_distance

I also modify the implementation such that it measures the distance by word, not by character.

To pre-translate the text for yourself:
```
python main.py
```

To run the data analysis for yourself:
```
python analysis.py
```

To run the unit tests:
```
python test.py
```

The text being translated is the entire prose of HG Wells' War of the Worlds. 🚀 All quotation marks have been removed from the text, as they caused encoding issues.

Preliminary results suggest that there is about a 30% difference in Google and DeepL's translations. This is far higher than I expected, as I'd been hoping to prove that any differences between the two were insignificant. I plan to adjust the methodology in the future.