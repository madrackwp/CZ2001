def bruteForce(text, pattern):
    patternLength = len(pattern)
    textLength = len(text)
    indexStart = 0
    indexEnd = patternLength
    indexArray = []

    while (indexEnd != len(text)+1):
        textToScan = str(text[indexStart:indexEnd])
        if (textToScan == pattern):
            indexArray.append(indexStart+1)
        indexStart += 1
        indexEnd += 1

    if (indexArray):
        print(indexArray)
    else:
        print("No matches found!")

