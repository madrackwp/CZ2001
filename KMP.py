# https://www.youtube.com/watch?v=4jY57Ehc14Y&ab_channel=WebofStories-LifeStoriesofRemarkablePeople
# https://www.geeksforgeeks.org/python-program-for-kmp-algorithm-for-pattern-searching-2/
import timeit
import time
# find longest prefix that is also a suffix


def computeLPSArray(pat, M, lps):
    length = 0
    i = 1
    lps[0] = 0  # lps for the first character will always be zero
    while i < M:  # M is the length of the array
        if pat[i] == pat[length]:
            # if the character at i equates to the character at length, we increase length by 1
            # lps of the character at i will be the new length, and then we increase the counter i
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # equate the length to be lps[len-1], and then check again
                # important to note that if we equate length=0, works for some sub strings but not all sub strings
                # will not work when there are many repeated characters in the string
                length = lps[length-1]
            else:
                # if length is already equals to zero, we just equate lps[i] to zero and increase the counter i
                lps[i] = 0
                i += 1


# text = "TTTATACCTTCCATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTTCGTCCGGGTGTGACCGAAAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTACGTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCACGTCAACATCTTAAAGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCCTCAACTTGAACAGCCCTATGTGTTCATCAAACGTTCGGATGCTCGAACTGCACCTCATGGTCATGTTATGGTTGAGCTGGTAGCAGAACTCGAAGGCATTCAGTACGGTCGTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGGCGAAATACCAGTGGCTTACCGCAAGGTTCTTCTTCGTAAGAACGGTAATAAAGGAGCTGGTGGCCATAGTTACGGCGCCGATCTAAAGTCATTTGACTTAGGCGACGAGCTTGGCACTGATCCTTATGAAGATTTTCAAGAAAACTGGAACACTAAACATAGCAGTGGTGTTACCCGTGAACTCATGCGTGAGCTTAACGGAGGGGCATACACTCGCTATTTATACCTTCC"
# text = open('genomeSequence2.txt', 'r').read().upper()
# pattern = "CACGACTGCTCGCT"
# pattern = "DAD" (to test failed case)
# create a list to record the indexes where matches are found

path = "C:\\Users\\user\\Desktop\\Repositories\\CZ2001\\ncbi-genomes-2020-09-11\\GCF_000006945.2_ASM694v2_genomic.fna"
# path = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001\\ncbi-genomes-2020-09-11\\GCF_000006945.2_ASM694v2_genomic.fna"
pattern = "CAAGCAAACTGATTCAAG"
f = open(path, "r")
fileStr = f.read()
f.close()

fileStr = fileStr.split("\n", 1)[1]
text = fileStr.replace("\n", "")


def KMPAlgo(text, pattern):
    indexList = []
    textLength = len(text)
    patternLength = len(pattern)
    # create an array for LPS
    lps = [0]*patternLength
    # compute LPS first
    computeLPSArray(pattern, patternLength, lps)
    print(lps)
    a = 0
    b = 0
    while a < textLength:
        if text[a] == pattern[b]:
            # match the pattern with the text, and the increase the counter a and b
            a += 1
            b += 1
        else:
            if b != 0:
                # equate b to lps[b-1], so we do not need to check from the beginning if there is an lps
                b = lps[b-1]
            else:
                a += 1
        if b == patternLength:
            # if b == patternLength, means entire pattern that matches has been found
            # append the index of the start of the pattern to the list
            indexList.append(a-b+1)
            b = lps[b-1]

    if not indexList:
        print("Pattern not found")
    else:
        print("Pattern found at Positions:", end=" ")
        print(indexList)


# KMPAlgo(text, pattern)
# print(timeit.timeit('KMPAlgo(text, pattern)',
#                     'from __main__ import KMPAlgo, text, pattern', number=1000))
before = time.time()
KMPAlgo(text, pattern)
after = time.time()
print(after-before)
