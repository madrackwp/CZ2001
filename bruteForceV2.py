# 1. Extract the part of the string to be tested
# 2. Compare the sliced string with the pattern
# 2.1 If the first char is the same, move on to the next char
# 2.2 If there is a char that is not the same, break out
# 3. If all the letters are similar, then add the index of the first char to the array to be printed

# This will be the text where the algorithm will scan the pattern for
# text = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCGCTA"
text = "ADADADADADADADADADADADADAD"
# This is the pattern that the algorithm will scan for
# pattern = "TTTATACCTTCC"
pattern = "DAD"

patternLength = len(pattern)
# print(patternLength)
textLength = len(text)
# print(textLength)

indexStart = 0
indexEnd = patternLength
indexList = list()
# print(type(indexList))

while (indexEnd != len(text)):
    textToScan = text[indexStart:indexEnd]
    # print(textToScan, len(textToScan))

    if (textToScan == pattern):
        print("SAME @ index: ", indexStart)
        indexList.append(indexStart+1)
    # else:
    #     print("DIFF")
    indexStart += 1
    indexEnd += 1

print(indexList)
