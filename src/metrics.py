import ctypes
import os
def levenshtein(s,t):
    # Load the DLL
    lev_dll = ctypes.WinDLL(os.path.dirname(__file__) + "\\levenshtein.dll")

    # Call the function from the DLL
    return lev_dll.levenshtein(s.encode('utf-8'), t.encode('utf-8'))