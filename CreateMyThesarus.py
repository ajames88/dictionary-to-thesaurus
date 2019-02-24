# Author: Austin James, All Rights Reserved

# WARNING:
# The program 'ParseThesarus.py' must be run in order to run
# this program.

# Read in the list of stopwords from 'stopwords.txt'

read = open("stopwords.txt", "r")

stopwords = []

for x in read:
    word = x.strip()
    stopwords.append(word.upper())

# The list of stopwords is now contained in the list stopwords
