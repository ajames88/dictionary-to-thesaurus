# Author: Austin James, All Rights Reserved

# WARNING:
# The program 'ParseThesarus.py' must be run in order to run
# this program.

import sys

# Read in the list of words and definitions for which to make a thesarus ------

letter = sys.argv[1]

dictionaryInputFile = "./ParsedDictionary/"+letter.upper()+".txt"

read = open(dictionaryInputFile, "r")

# -----------------------------------------------------------------------------

# Compare against all definitions to find synonyms ----------------------------

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for x in alphabet:
    dictionaryFile = "./ParsedDictionary/"+x+".txt"
    read = open(dictionaryFile)

# -----------------------------------------------------------------------------
