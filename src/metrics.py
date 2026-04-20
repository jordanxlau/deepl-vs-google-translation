import ctypes
import os

# Load the DLLs
meteor_dll = ctypes.CDLL(os.path.dirname(__file__) + "\\meteor.dll")
lev_dll = ctypes.WinDLL(os.path.dirname(__file__) + "\\levenshtein.dll")

# Set resolution types
meteor_dll.meteor.restype = ctypes.c_double

def levenshtein(s,t):
    # Call the levenshtein distance function from the DLL
    return lev_dll.levenshtein(s.encode('utf-8'), t.encode('utf-8'))

def meteor(s,t):
    # Call the meteor function from the DLL
    return meteor_dll.meteor(s.encode('utf-8'), t.encode('utf-8'))
