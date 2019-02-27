# Author: Austin James, All Rights Reserved

import sys

letter = sys.argv[1]

outputFile = letter+"output.txt"

writer = open(outputFile, "w")

writer.write("Thesaurus was generated for the letter "+letter+"\n\n")
writer.write("TERM\t\t\t# OF GENERATED SYNONYMS\t\t# OF COMMON SYNONYMS")
writer.write("\t\t% OF CORRECT GENERATED SYNONYMS\n")

# Read in the list of Moby thesaurus entries for all the words beginning with
# the given letter ------------------------------------------------------------

read = open("mobythesarus.txt", "r")

mobyThesaurus = []

for x in read:
    if (x[0] == letter):
        entry = x.split(",")
        term = entry[0].upper()
        synonyms = []
        for x in range(len(entry)-1):
            synonym = entry[x+1].upper()
            synonyms.append(synonym.strip())
        entry = [term, synonyms]
        mobyThesaurus.append(entry)

# -----------------------------------------------------------------------------


# Read in the generated thesaurus entries for all the words beginning with the
# given letter ----------------------------------------------------------------

generatedThesaurusFile = "thesaurusFor"+letter+".txt"

read = open(generatedThesaurusFile, "r")

generatedThesaurus = []

for x in read:
    generatedThesaurus.append(x)

# -----------------------------------------------------------------------------

# Compare the entries from both thesauruses -----------------------------------

for x in generatedThesaurus:
    endOfTerm = x.index("SYNONYMS")
    term = x[5:(endOfTerm-1)]
    synonyms = x[(endOfTerm+10):(len(x)-1)].split()
    for y in mobyThesaurus:
        mobyTerm = y[0]
        mobySynonyms = y[1]
        if (term == mobyTerm) and (len(synonyms) > 0):
            common = 0
            for z in synonyms:
                if mobySynonyms.count(z) > 0:
                    common = common + 1
            percentCorrect = float(common)/float(len(synonyms))
            output = term+"\t\t\t\t\t"+str(len(synonyms))+"\t\t\t\t\t\t"
            output = output+str(common)+"\t\t\t\t\t\t"+str(percentCorrect)
            writer.write(output+"\n")

# -----------------------------------------------------------------------------
