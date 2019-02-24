read = open("stopwords.txt", "r")

stopwords = []

for x in read:
    word = x.strip()
    stopwords.append(word.upper())

print(stopwords)
