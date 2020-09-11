import timeit


def hashing(toHash):
    length = len(toHash)
    hashcode = 0
    for x in range(length):
        characterValue = ord(toHash[x])
        position = length - x - 1
        hashcode += characterValue*10**position
    return hashcode


def rehash(toRehash, lengthOfPattern, hashValue):
    valueOfFirst = ord(toRehash[0])*10**(lengthOfPattern-1)
    valueOfLast = ord(toRehash[lengthOfPattern-1])
    hashValue = hashValue - valueOfFirst
    hashValue *= 10
    hashValue += valueOfLast
    return hashValue


def v1(text, pattern):
    patternHash = hashing(pattern)
    indexArray = []
    # print(patternHash)
    for x in range(len(text)):
        textToScan = text[x:len(pattern)+x]
        if (len(textToScan) != len(pattern)):
            break
        textHash = hashing(textToScan)
        if (textHash == patternHash):
            # print("found!")
            indexArray.append(x)
        # else:
        #     print("Not found")
    print(indexArray)


def v2(text, pattern):
    patternHash = hashing(pattern)
    indexArray = []
    textToScan = text[0:len(pattern)]
    textHash = hashing(textToScan)
    index = 0
    while (index != len(text)-len(pattern)):
        if (patternHash == textHash):
            indexArray.append(index)
            oldChar = textToScan[0]
            index += 1
            textToScan = text[index: len(pattern)+index]
            newChar = textToScan[-1]
            textHash -= ord(oldChar)*(10**(len(pattern)-1))
            textHash *= 10
            textHash += ord(newChar)
        else:
            oldChar = textToScan[0]
            index += 1
            textToScan = text[index: len(pattern)+index]
            newChar = textToScan[-1]
            textHash -= ord(oldChar)*(10**(len(pattern)-1))
            textHash *= 10
            textHash += ord(newChar)
    print(indexArray)


text = "TTTATACCTTCCATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTTCGTCCGGGTGTGACCGAAAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTACGTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCACGTCAACATCTTAAAGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCCTCAACTTGAACAGCCCTATGTGTTCATCAAACGTTCGGATGCTCGAACTGCACCTCATGGTCATGTTATGGTTGAGCTGGTAGCAGAACTCGAAGGCATTCAGTACGGTCGTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGGCGAAATACCAGTGGCTTACCGCAAGGTTCTTCTTCGTAAGAACGGTAATAAAGGAGCTGGTGGCCATAGTTACGGCGCCGATCTAAAGTCATTTGACTTAGGCGACGAGCTTGGCACTGATCCTTATGAAGATTTTCAAGAAAACTGGAACACTAAACATAGCAGTGGTGTTACCCGTGAACTCATGCGTGAGCTTAACGGAGGGGCATACACTCGCTATTTATACCTTCC"
# text = "TTTATACCTTCCCG"
pattern = "TTTATACCTTCC"
# text = "ABCDEFGHGFEDCBCDA"
# pattern = "BCD"
# print(timeit.timeit('v1(text, pattern)',
#                     'from __main__ import v1, text, pattern', number=1000))

# print(timeit.timeit('v2(text, pattern)',
#                     'from __main__ import v2, text, pattern', number=1000))

v2(text, pattern)
v1(text, pattern)
