# https://www.geeksforgeeks.org/real-time-optimized-kmp-algorithm-for-pattern-searching/

import numpy as np
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

# compute failure table


def computeFailureTable(characters, pattern, lps, FT):
    j = 0
    for i in characters:
        l = 0
        while l < length:
            if pattern[lps[l]] == i:
                # check if the pattern[lps[i]] is the particular character, if so, just add 1 to lps[1] for corresponding FT
                FT[j][l] = lps[l] + 1
            else:
                # if lps[l] is 0, then corresponding ft is 0 as well
                if lps[l] == 0:
                    FT[j][l] = 0
                # else, similar logic to lps, it will be equals to ft[lps[l]-1]
                else:
                    FT[j][l] = FT[j][lps[l]-1]
            l += 1
        j += 1
    FT.astype(int)
    # convert to dictionary where each character is a key, and the array is the corresponding value
    dictionary = {characters[i]: FT[i] for i in range(len(characters))}
    for key in dictionary:
        dictionary[key] = (dictionary[key]).astype(int)
    return dictionary

# print failure table


def printFailureTable(lps, dictionary):
    print(lps)
    for key in dictionary:
        print(key, dictionary[key])


def ImprovedKMPAlgo(text, pattern, dictionary):
    indexList = []
    textLength = len(text)
    patternLength = len(pattern)
    a = 0
    b = 0
    while a < textLength:
        if text[a] == pattern[b]:
            # match the pattern with the text, and the increase the counter a and b
            a += 1
            b += 1
        else:
            if b != 0:
                if text[a] not in dictionary:
                    # if the character at text index is not in the pattern, instantly move on to check next character
                    b = 0
                else:
                    # update j to be the longest suffix which is also a prefix of the pattern
                    b = (dictionary[text[a]])[b-1]
                a += 1
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
<<<<<<< HEAD
=======

>>>>>>> 6cb78a2a7fe99b0220f13748468577b5008db2a7

# text = open('genomeSequence2.txt', 'r').read().upper()
# pattern = "TGACCTATGAT"
# text = "TTTATACCTTCCATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTTCGTCCGGGTGTGACCGAAAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTACGTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCACGTCAACATCTTAAAGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCCTCAACTTGAACAGCCCTATGTGTTCATCAAACGTTCGGATGCTCGAACTGCACCTCATGGTCATGTTATGGTTGAGCTGGTAGCAGAACTCGAAGGCATTCAGTACGGTCGTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGGCGAAATACCAGTGGCTTACCGCAAGGTTCTTCTTCGTAAGAACGGTAATAAAGGAGCTGGTGGCCATAGTTACGGCGCCGATCTAAAGTCATTTGACTTAGGCGACGAGCTTGGCACTGATCCTTATGAAGATTTTCAAGAAAACTGGAACACTAAACATAGCAGTGGTGTTACCCGTGAACTCATGCGTGAGCTTAACGGAGGGGCATACACTCGCTATTTATACCTTCC"
path = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001\\ncbi-genomes-2020-09-11\\GCF_000006945.2_ASM694v2_genomic.fna"
pattern = "AAAACCGACGGTC"
f = open(path, "r")
fileStr = f.read()
f.close()

fileStr = fileStr.split("\n", 1)[1]
text = fileStr.replace("\n", "")
before = time.time()
length = len(pattern)
characters = list(set(pattern))
len_characters = len(characters)
lps = [0]*length
computeLPSArray(pattern, length, lps)
FT = np.empty((len_characters, length))
my_dict = computeFailureTable(characters, pattern, lps, FT)
<<<<<<< HEAD
printFailureTable(lps,my_dict)
=======
printFailureTable(lps, my_dict)
>>>>>>> 6cb78a2a7fe99b0220f13748468577b5008db2a7
ImprovedKMPAlgo(text, pattern, my_dict)
after = time.time()
print(after-before)


<<<<<<< HEAD
# print(timeit.timeit('ImprovedKMPAlgo(text, pattern, my_dict)',
                    # 'from __main__ import ImprovedKMPAlgo, text, pattern, my_dict', number=1000))
=======
# print("Average time for 1000 iterations: {}".format(timeit.timeit('ImprovedKMPAlgo(text, pattern, my_dict)',
#   'from __main__ import ImprovedKMPAlgo, text, pattern, my_dict', number=1000)/1000))
>>>>>>> 6cb78a2a7fe99b0220f13748468577b5008db2a7
