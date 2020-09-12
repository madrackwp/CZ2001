import timeit
import time


def hashing(toHash):
    length = len(toHash)
    hashcode = 0
    for x in range(length):
        characterValue = ord(toHash[x])
        position = length - x - 1
        hashcode += characterValue*10**position
    return hashcode


# def rehash(toRehash, lengthOfPattern, hashValue):
#     valueOfFirst = ord(toRehash[0])*10**(lengthOfPattern-1)
#     valueOfLast = ord(toRehash[lengthOfPattern-1])
#     hashValue = hashValue - valueOfFirst
#     hashValue *= 10
#     hashValue += valueOfLast
#     return hashValue

def search(pat, txt, q):
    indexArray = []
    d = 256
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*d) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break

            j += 1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                indexArray.append(i)
            #     print("Pattern found at index " + str(i) )

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t+q


def RKNaive(text, pattern):
    patternHash = hashing(pattern)
    indexArray = []
    sturiousHits = 0
    # print(patternHash)
    for x in range(len(text)):
        textToScan = text[x:len(pattern)+x]
        if (len(textToScan) != len(pattern)):
            break
        textHash = hashing(textToScan)
        if (textHash == patternHash):
            print("Hit")
            if (pattern == textToScan):
                print("found!")
                indexArray.append(x)
            else:
                print("Sturious Hit")
                sturiousHits += 1
        # else:
        #     print("Not found")
    print(indexArray)
    print(sturiousHits)


def RKRollingHash(text, pattern):
    sturiousHits = 0
    patternHash = hashing(pattern)
    indexArray = []
    textToScan = text[0:len(pattern)]
    textHash = hashing(textToScan)
    textLen = len(text)
    patternLen = len(pattern)
    index = 0
    while (index != textLen-patternLen+1):
        if (patternHash == textHash):
            if (textToScan == pattern):
                indexArray.append(index)
            else:
                sturiousHits += 1

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
    # print(indexArray)
    # print("No. of sturious hits: {}".format(sturiousHits))


# text = "TTTATACCTTCCATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTTCGTCCGGGTGTGACCGAAAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTACGTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCACGTCAACATCTTAAAGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCCTCAACTTGAACAGCCCTATGTGTTCATCAAACGTTCGGATGCTCGAACTGCACCTCATGGTCATGTTATGGTTGAGCTGGTAGCAGAACTCGAAGGCATTCAGTACGGTCGTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGGCGAAATACCAGTGGCTTACCGCAAGGTTCTTCTTCGTAAGAACGGTAATAAAGGAGCTGGTGGCCATAGTTACGGCGCCGATCTAAAGTCATTTGACTTAGGCGACGAGCTTGGCACTGATCCTTATGAAGATTTTCAAGAAAACTGGAACACTAAACATAGCAGTGGTGTTACCCGTGAACTCATGCGTGAGCTTAACGGAGGGGCATACACTCGCTATTTATACCTTCC"
# text = "TTTATACCTTCCCG"
text = open('genomeSequence.txt', 'r').read().upper()
pattern = "TGACCTATGAT"
q = 29
# text = "ABCDEFGHGFEDCBCDA"
# pattern = "BCD"
# print(timeit.timeit('RKNaive(text, pattern)',
#                     'from __main__ import RKNaive, text, pattern', number=1000))

# print("Average time for 1000 iterations: {}".format(timeit.timeit('search(text, pattern, q)',
#                                                                   'from __main__ import search, text, pattern, q', number=1000)/1000))
before = time.time()
# # # RKNaive(text, pattern)
# # RKRollingHash(text, pattern)
search(pattern, text, 29)
after = time.time()
print(after-before)
