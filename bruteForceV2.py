import time

text = open('genomeSequence2.txt', 'r').read().upper()
# This is the pattern that the algorithm will scan for
pattern = "TGACCTATGAT"
# pattern = "DAD"


def bruteForce(text, pattern):
    patternLength = len(pattern)

    textLength = len(text)

    indexStart = 0
    indexEnd = patternLength
    indexArray = []

    while (indexEnd != len(text)+1):
        textToScan = text[indexStart:indexEnd]

        if (textToScan == pattern):
            indexArray.append(indexStart+1)
        indexStart += 1
        indexEnd += 1

    print(indexArray)


before = time.time()
bruteForce(text, pattern)
after = time.time()
print(after-before)
