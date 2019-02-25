# Author: Austin James, All Rights Reserved

import sys

# Read in the list of synonyms for all the words beginning with the given letter

read = open("mobythesarus.txt", "r")

letter = sys.argv[1]

thesaurus = []

for x in read:
    if (x[0] == letter):
        entry = x.split(",")
        term = entry[0]
        synonyms = []
        for x in range(len(entry)-1):
            synonyms.append(entry[x+1].strip())
        entry = [term, synonyms]
        thesaurus.append(entry)

# -----------------------------------------------------------------------------
