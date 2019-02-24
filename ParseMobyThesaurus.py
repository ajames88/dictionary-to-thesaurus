# Author: Austin James, All Rights Reserved

# This file takes in the list of thesarus entries taken
# from the Moby thesarus and prints them to an output
# file 'thesarus.txt' with each entry on its own line.
# All entries are stripped of whitespace and printed
# in UPPER CASE.

# Reader to read in entries from 'words.txt'
read = open("words.txt", "r")

# Writer to print output to 'thesarus.txt'
writer = open("mobythesarus.txt", "w")

for x in read:
  entry = x.strip()
  writer.write(x.upper())
  writer.write("\n")
