# Author: Austin James, All Rights Reserved

# WARNING:
# The program 'ParseThesarus.py' and 'ParsedDictionary.py' must be run in
# order to run this program.

print("\n")

import sys
import math
import timeit

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Initialize the vector space list and the default vector ---------------------

vectorDimensions = []
vectors = []

numDefinitions = 0

wordList = []

comparisonDictionary = []
comparisonVectors = []

start = timeit.default_timer()

for x in alphabet:
    dictionaryFile = "./ParsedDictionary/"+x+".txt"
    read = open(dictionaryFile)
    for y in read:
        if y.count("TERM") > 0:
            numDefinitions = numDefinitions + 1
            endOfTerm = y.index("DEF")
            term = y[5:(endOfTerm-1)]
            definition = y[endOfTerm+4:(len(y)-1)].split()
            for z in definition:
                wordList.append(z)
            if len(definition) > 0:
                entry = []
                entry.append(term)
                entry.append(definition)
                comparisonDictionary.append(entry)

vectorDimensions = list(dict.fromkeys(wordList))

stop = timeit.default_timer()
time = stop - start

print("Vector Dimesnions computed (" + str(time) + " s)")
# -----------------------------------------------------------------------------

# Read in the list of words and definitions for which to make a thesarus ------

letter = sys.argv[1]

dictionaryInputFile = "./ParsedDictionary/"+letter.upper()+".txt"

read = open(dictionaryInputFile, "r")

dictionary = []

start = timeit.default_timer()

for x in read:
    if x.count("TERM") > 0:
        endOfTerm = x.index("DEF")
        term = x[5:endOfTerm-1]
        definition = x[endOfTerm+4:(len(x)-1)].split()

        entry = []
        entry.append(term)
        entry.append(definition)

        if len(definition) > 0:
            dictionary.append(entry)

stop = timeit.default_timer()
time = stop - start

print(letter + " dictionary loaded (" + str(time) + " s)")

# The terms we are making a thesaurus for and their definitions are now in the
# list dictionary -------------------------------------------------------------

# Find the frequency with which each word appears in the dictionary -----------

start = timeit.default_timer()

dictionaryFreqs = {}

for x in wordList:
    if x.upper() not in dictionaryFreqs:
        dictionaryFreqs[x.upper()] = 1
    else:
        dictionaryFreqs[x.upper()] = dictionaryFreqs[x.upper()] + 1

stop = timeit.default_timer()
time = stop - start

print("Word Frequencies found (" + str(time) + " s)")

start = timeit.default_timer()

idfValues = {}

dividend = ( 1 + math.log10(numDefinitions) )

for x, y in dictionaryFreqs.items():
    idfValues[x] = dividend/y

stop = timeit.default_timer()
time = stop - start

print("IDF Values computed (" + str(time) + " s)")

# -----------------------------------------------------------------------------

# Create the list of vectors for each term in the dictionary ------------------

start = timeit.default_timer()

for x in range(len(dictionary)):

    vec = {}

    item = dictionary[x]

    for y in item[1]:
        if y.upper() in vec:
            vec[y.upper()] = vec[y.upper()] + (1 * idfValues[y.upper()])
        else:
            vec[y.upper()] = (1 * idfValues[y.upper()])

    vectors.append([item[0],vec])

for x in range(len(comparisonDictionary)):

    defaultVector = {}

    vec = {}

    item = comparisonDictionary[x]

    for y in item[1]:
        if y.upper() in vec:
            vec[y.upper()] = vec[y.upper()] + (1 * idfValues[y.upper()])
        else:
            vec[y.upper()] = (1 * idfValues[y.upper()])

    comparisonVectors.append([item[0],vec])

stop = timeit.default_timer()
time = stop - start
print("Frequency vectors created (" + str(time) + " s)")

# -----------------------------------------------------------------------------

# Normalize all the vectors ---------------------------------------------------

start = timeit.default_timer()

for x in vectors:
    sum = 0.0
    for y, z in x[1].items():
        sum = (sum + (z * z))
    root = math.sqrt(sum)
    normfactor = (float(1) / root)
    for y, z in x[1].items():
        x[1][y] = (float(x[1][y]) * normfactor)

for x in comparisonVectors:
    sum = 0.0
    for y, z in x[1].items():
        sum = (sum + (z * z))
    root = math.sqrt(sum)
    normfactor = (float(1) / root)
    for y, z in x[1].items():
        x[1][y] = (float(x[1][y]) * normfactor)

stop = timeit.default_timer()
time = stop - start
print("Normalized vectors (" + str(time) + " s)")

# -----------------------------------------------------------------------------

# Compute cosine similarities of all documents to all other documents ---------

start = timeit.default_timer()

synonyms = {}

for x in dictionary:
    synonyms[x[0]] = {}

acceptableSimilarity = 0.4
identicalSimilarity = 0.95

for x in vectors:
    for y in comparisonVectors:
        similarity = 0.0
        for t, v in x[1].items():
            if t in y[1]:
                similarity = (similarity + (v * y[1][t]))
        if (similarity >= acceptableSimilarity) and (similarity < identicalSimilarity):
            synonyms[x[0]][y[0]] = similarity

stop = timeit.default_timer()
time = stop - start
print("Computed cosine similarity and found synonyms (" + str(time) + " s)")

# -----------------------------------------------------------------------------

# Writer to write thesaurus to output file ------------------------------------

outputFile = "thesaurusFor"+letter+".txt"

writer = open(outputFile, "w")

# -----------------------------------------------------------------------------

# Print to Output -------------------------------------------------------------

start = timeit.default_timer()

for x in dictionary:
    if len(synonyms[x[0]]) > 0:
        writer.write("TERM "+str(x[0]).upper()+" SYNONYMS")
        for y in synonyms[x[0]]:
            writer.write(" "+str(y.upper()))
        writer.write("\n")

stop = timeit.default_timer()
time = stop - start
print("Thesaurus written to output (" + str(time) + " s)")

# -----------------------------------------------------------------------------

print("\n")
