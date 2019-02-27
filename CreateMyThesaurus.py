# Author: Austin James, All Rights Reserved

# WARNING:
# The program 'ParseThesarus.py' and 'ParsedDictionary.py' must be run in
# order to run this program.

import sys

# Read in the list of words and definitions for which to make a thesarus ------

letter = sys.argv[1]

dictionaryInputFile = "./ParsedDictionary/"+letter.upper()+".txt"

read = open(dictionaryInputFile, "r")

dictionary = []

for x in read:
    if x.count("TERM") > 0:
        endOfTerm = x.index("DEF")
        term = x[5:endOfTerm-1]
        definition = x[endOfTerm+4:(len(x)-1)].split()
        entry = []
        entry.append(term)
        entry.append(definition)
        dictionary.append(entry)

# The terms we are making a thesaurus for and their definitions are now in the
# list dictionary -------------------------------------------------------------

# Writer to write thesaurus to output file ------------------------------------

outputFile = "thesaurusFor"+letter+".txt"

writer = open(outputFile, "w")

# -----------------------------------------------------------------------------

# Compare against all definitions to find synonyms ----------------------------

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

synonyms = []

for x in dictionary:
    synonyms.append([x[0]])

for x in alphabet:
    dictionaryFile = "./ParsedDictionary/"+x+".txt"
    read = open(dictionaryFile)
    comparisonDictionary = []
    for x in read:
        if x.count("TERM") > 0:
            endOfTerm = x.index("DEF")
            term = x[5:(endOfTerm-1)]
            definition = x[endOfTerm+4:(len(x)-1)].split()
            entry = []
            entry.append(term)
            entry.append(definition)
            comparisonDictionary.append(entry)
    for x in range(len(dictionary)):
        term = dictionary[x][0]
        definition = dictionary[x][1]
        entry = [term]
        for y in comparisonDictionary:
            similarWords = 0
            comparisonTerm = y[0]
            comparisonDefinition = y[1]
            for z in definition:
                if comparisonDefinition.count(z) > 0:
                    similarWords = similarWords + 1
            if similarWords > (len(definition)/2) and (comparisonTerm != term):
                synonyms[x].append(comparisonTerm)

# -----------------------------------------------------------------------------

# Print to Output -------------------------------------------------------------

for x in synonyms:
    writer.write("TERM "+str(x[0]).upper()+" SYNONYMS")
    for y in range(len(x)-1):
        writer.write(" "+str(x[y+1]).upper())
    writer.write("\n")

# -----------------------------------------------------------------------------
