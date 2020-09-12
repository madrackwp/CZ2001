import timeit
import time

# 1. Extract the part of the string to be tested
# 2. Compare the sliced string with the pattern
# 2.1 If the first char is the same, move on to the next char
# 2.2 If there is a char that is not the same, break out
# 3. If all the letters are similar, then add the index of the first char to the array to be printed

# This will be the text where the algorithm will scan the pattern for
# text = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCGCTA"
# text = "ADADADADADADADADADADADADAD"
# text = "TTTATACCTTCCATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTTCGTCCGGGTGTGACCGAAAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTACGTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCACGTCAACATCTTAAAGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCCTCAACTTGAACAGCCCTATGTGTTCATCAAACGTTCGGATGCTCGAACTGCACCTCATGGTCATGTTATGGTTGAGCTGGTAGCAGAACTCGAAGGCATTCAGTACGGTCGTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGGCGAAATACCAGTGGCTTACCGCAAGGTTCTTCTTCGTAAGAACGGTAATAAAGGAGCTGGTGGCCATAGTTACGGCGCCGATCTAAAGTCATTTGACTTAGGCGACGAGCTTGGCACTGATCCTTATGAAGATTTTCAAGAAAACTGGAACACTAAACATAGCAGTGGTGTTACCCGTGAACTCATGCGTGAGCTTAACGGAGGGGCATACACTCGCTATTTATACCTTCC"
# Added 2 more patterns to front and back of text
text = open('genomeSequence.txt', 'r').read().upper()
# This is the pattern that the algorithm will scan for
pattern = "TGACCTATGAT"
# pattern = "DAD"


def bruteForce(text, pattern):
    patternLength = len(pattern)

    textLength = len(text)

    indexStart = 0
    indexEnd = patternLength
    indexList = list()

    while (indexEnd != len(text)+1):
        textToScan = text[indexStart:indexEnd]

        if (textToScan == pattern):
            indexList.append(indexStart+1)
        indexStart += 1
        indexEnd += 1


print("Average time for 1000 iterations: {}".format(timeit.timeit('bruteForce(text, pattern)',
                                                                  'from __main__ import bruteForce, text, pattern', number=1000)/1000))

# before = time.time()
# bruteForce(text, pattern)
# after = time.time()
# print(after-before)
