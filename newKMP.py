import numpy as np

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

def computeFailureTable(characters, pattern, lps, FT): 
    j = 0
    for i in characters: 
        l = 0
        while l < length: 
            if pattern[lps[l]] == i: 
                FT[j][l] = lps[l] + 1
            else: 
                if lps[l] == 0: 
                    FT[j][l] = 0
                else: 
                    FT[j][l] = FT[j][lps[l]-1]
            l += 1
        j += 1

def printFailureTable(characters, FT): 
    for i in range(len(characters)): 
        print(characters[i], end=" ")
        print(FT[i])

text = "TTTATACCTTCCATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTTCGTCCGGGTGTGACCGAAAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTACGTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCACGTCAACATCTTAAAGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCCTCAACTTGAACAGCCCTATGTGTTCATCAAACGTTCGGATGCTCGAACTGCACCTCATGGTCATGTTATGGTTGAGCTGGTAGCAGAACTCGAAGGCATTCAGTACGGTCGTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGGCGAAATACCAGTGGCTTACCGCAAGGTTCTTCTTCGTAAGAACGGTAATAAAGGAGCTGGTGGCCATAGTTACGGCGCCGATCTAAAGTCATTTGACTTAGGCGACGAGCTTGGCACTGATCCTTATGAAGATTTTCAAGAAAACTGGAACACTAAACATAGCAGTGGTGTTACCCGTGAACTCATGCGTGAGCTTAACGGAGGGGCATACACTCGCTATTTATACCTTCC"
pattern = "TTTATACCTTCC"
length = len(pattern)
characters = list(set(text))
len_characters = len(characters)
lps = [0]*length
computeLPSArray(pattern, length, lps)
FT = np.empty((len_characters,length))
computeFailureTable(characters, pattern, lps, FT)
printFailureTable(characters, FT)