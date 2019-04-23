# Author: Austin James, All Rights Reserved

# WARNING:
# The program 'ParseThesarus.py' and 'ParsedDictionary.py' must be run in
# order to run this program.

import sys
import math

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Initialize the vector space list and the default vector ---------------------

vectorDimensions = []
vectors = []

# -----------------------------------------------------------------------------

# Read in the list of words and definitions for which to make a thesarus ------

letter = sys.argv[1]

dictionaryInputFile = "./ParsedDictionary/"+letter.upper()+".txt"

read = open(dictionaryInputFile, "r")

dictionary = []
wordList = []

for x in read:
    if x.count("TERM") > 0:
        endOfTerm = x.index("DEF")
        term = x[5:endOfTerm-1]
        definition = x[endOfTerm+4:(len(x)-1)].split()

        entry = []
        entry.append(term)
        entry.append(definition)

        for y in definition:
            wordList.append(y.upper())
            if y.upper() not in vectorDimensions:
                vectorDimensions.append(y.upper())

        if len(definition) > 0:
            dictionary.append(entry)

# The terms we are making a thesaurus for and their definitions are now in the
# list dictionary -------------------------------------------------------------

# Find the frequency with which each word appears in the dictionary -----------

dictionaryFreqs = []

for y in vectorDimensions:
    dictionaryFreqs.append([y,0])

for x in wordList:
    i = vectorDimensions.index(x)
    dictionaryFreqs[i][1] = dictionaryFreqs[i][1] + 1

idfValues = []

for x in dictionaryFreqs:
    idfValues.append([x[0],(1+math.log10((len(dictionary)/x[1])))])

# -----------------------------------------------------------------------------

# Create the list of vectors for each term in the dictionary ------------------

for x in range(len(dictionary)):

    defaultVector = []
    for y in vectorDimensions:
        defaultVector.append([y,0])

    for y in dictionary[x][1]:
        i = vectorDimensions.index(y.upper())
        defaultVector[i][1] = defaultVector[i][1] + 1
        vectors.append(defaultVector)

print("\nFreqs\n")
print(vectors[0])
# -----------------------------------------------------------------------------

# Multiply each term in each vector by its idf value --------------------------

dictionaryWords = []

for x in dictionaryFreqs:
    dictionaryWords.append(x[0])

tfidfVectors = []

for x in vectors:
    vec = []
    for y in x:
        i = dictionaryWords.index(y[0])
        temp = y[1]*idfValues[i][1]
        vec.append([y[0], temp])
    tfidfVectors.append(vec)


print("\nFreqs with idfs\n")
print(tfidfVectors[0])
# -----------------------------------------------------------------------------

# Normalize all the vectors ---------------------------------------------------

for x in vectors:
    sum = 0.0
    for y in x:
        sum += y[1]*y[1]
    normfactor = math.sqrt(sum)
    normfactor = 1/normfactor
    for y in range(len(x)):
        x[y][1] = float(x[y][1])*normfactor

# -----------------------------------------------------------------------------

# Writer to write thesaurus to output file ------------------------------------

outputFile = "thesaurusFor"+letter+".txt"

writer = open(outputFile, "w")

# -----------------------------------------------------------------------------

# Compare against all definitions to find synonyms ----------------------------

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
