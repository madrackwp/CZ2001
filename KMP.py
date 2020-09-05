# https://www.youtube.com/watch?v=4jY57Ehc14Y&ab_channel=WebofStories-LifeStoriesofRemarkablePeople
# https://www.geeksforgeeks.org/python-program-for-kmp-algorithm-for-pattern-searching-2/


def computeLPSArray (pat,M,lps): 
    len = 0
    i = 1
    lps[0]=0
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else: 
            if len != 0: 
                len = lps[len-1]
            else: 
                lps[i] = 0
                i+=1

text = "TTTATACCTTCCATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTTCGTCCGGGTGTGACCGAAAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTACGTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCACGTCAACATCTTAAAGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCCTCAACTTGAACAGCCCTATGTGTTCATCAAACGTTCGGATGCTCGAACTGCACCTCATGGTCATGTTATGGTTGAGCTGGTAGCAGAACTCGAAGGCATTCAGTACGGTCGTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGGCGAAATACCAGTGGCTTACCGCAAGGTTCTTCTTCGTAAGAACGGTAATAAAGGAGCTGGTGGCCATAGTTACGGCGCCGATCTAAAGTCATTTGACTTAGGCGACGAGCTTGGCACTGATCCTTATGAAGATTTTCAAGAAAACTGGAACACTAAACATAGCAGTGGTGTTACCCGTGAACTCATGCGTGAGCTTAACGGAGGGGCATACACTCGCTATTTATACCTTCC"
pattern = "TTTATACCTTCC"
# pattern = "DAD"
indexList = []

textLength = len(text)
patternLength = len(pattern)
lps = [0]*patternLength
computeLPSArray (pattern,patternLength,lps)
i = 0
j = 0
while i < textLength: 
    if text[i] == pattern[j]: 
        i += 1
        j += 1
    else: 
        if j != 0:
            j = lps[j-1]
        else:
            i += 1
    if j==patternLength: 
        indexList.append(i-j+1)
        j = lps[j-1]

if not indexList: 
    print("Pattern not found")
else: 
    print("Pattern found at Positions:", end= " ")
    print(indexList)
