import ctypes
import os

# to compile to .dll, use `go build -buildmode=c-shared -o file.dll file.go`
# if gcc not found, use `export PATH="/c/msys64/ucrt64/bin:$PATH"`

# Load the DLLs
meteor_dll = ctypes.WinDLL(os.path.dirname(__file__) + "\\meteor.dll")
lev_dll = ctypes.WinDLL(os.path.dirname(__file__) + "\\levenshtein.dll")

# Set resolution types
meteor_dll.Meteor.restype = ctypes.c_double

def levenshtein(s,t):
    # Call the levenshtein distance function from the DLL
    return lev_dll.Levenshtein(s.encode('utf-8'), t.encode('utf-8'))

def meteor(s,t):
    # Call the meteor function from the DLL
    return meteor_dll.Meteor(s.encode('utf-8'), t.encode('utf-8'))
