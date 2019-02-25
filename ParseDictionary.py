# Author: Austin James, All Rights Reserved

import sys

# Read in the list of stopwords from 'stopwords.txt' --------------------------

read = open("stopwords.txt", "r")

stopwords = []

for x in read:
    word = x.strip()
    stopwords.append(word.upper())

# The list of stopwords is now contained in the list stopwords ----------------


# Declare the list numbers, all terms in this list will be removed from
# definitions (all entries must be in UPPER CASE)------------------------------

numbers = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT",
        "NINE", "TEN"]

# -----------------------------------------------------------------------------


# removeStops function takes in a definition as its parameter and returns the
# same definition with no stop words, hypens, or periods ----------------------

def removeStops(definition):

    for x in range(len(definition)):
        word = definition[x].upper()
        if stopwords.count(word) > 0:
            definition[x] = ""

    numStopwords = definition.count("")

    for x in range(numStopwords):
        definition.remove("")

    numHyphens = definition.count("--")

    for x in range(numHyphens):
        definition.remove("--")

    for x in range(len(definition)):
        if definition[x].count(".") > 0:
            definition[x] = definition[x].replace(".", "")

    return definition
# -----------------------------------------------------------------------------

# removeStops function takes in a definition as its parameter and returns the
# same definition without the elements in the list numbers --------------------

def removeNums(definition):

    for x in range(len(definition)):
        word = definition[x].upper()
        if numbers.count(word) > 0:
            definition[x] = ""

    numNums = definition.count("")

    for x in range(numNums):
        definition.remove("")

    return definition
# -----------------------------------------------------------------------------


# stripTags function takes in a definition as its parameter and returns the
# same definition with no tags ------------------------------------------------

def stripTags(definition):

    for x in range(len(definition)):
        if definition[x].count("<") > 0:
            definition[x] = ""

    numTags = definition.count("")

    for x in range(numTags):
        definition.remove("")

    return definition

# -----------------------------------------------------------------------------


# sys.argv[1] contains the value of the letter whose entries are to be parsed
letter = sys.argv[1]

dictionaryInputFile = "./gcide-0.52/CIDE."+letter.upper()
read = open(dictionaryInputFile, "r")

dictionaryOutputFile = "./ParsedDictionary/"+letter.upper()+".txt"
writer = open(dictionaryOutputFile, "w")


for x in read:

    entry = ""

    # Parse the term
    if (x.find("<ent>") >= 0):
        termStart = x.find("<ent>") + 5
        termEnd = x.find("</ent>")
        term = x[termStart:termEnd]
        entry += "\n\nTERM "+term+":\n"

    # Parse the definition
    if (x.find("<def>") >= 0):
        definitionStart = x.find("<def>") + 5
        definitionEnd = x.find("</def>")
        definition = x[definitionStart:definitionEnd]
        definition = definition.split()
        # Remove stopwords from the definition
        definition = removeStops(definition)
        # Remove numbers from the definition
        definition = removeNums(definition)
        # Remove tags from the definition
        definition = stripTags(definition)
        for x in definition:
            entry += x+" "

    writer.write(entry)
