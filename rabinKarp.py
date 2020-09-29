import timeit
import time
# from Bio import SeqIO


def hashing(toHash, alphabetSize):
    length = len(toHash)
    hashcode = 0
    for x in range(length):
        characterValue = ord(toHash[x])
        position = length - x - 1
        hashcode += characterValue*alphabetSize**position
    return hashcode


# def RKNaive(text, pattern):
#     patternHash = hashing(pattern)
#     indexArray = []
#     sturiousHits = 0
#     # print(patternHash)
#     for x in range(len(text)):
#         textToScan = text[x:len(pattern)+x]
#         if (len(textToScan) != len(pattern)):
#             break
#         textHash = hashing(textToScan)
#         if (textHash == patternHash):
#             print("Hit")
#             if (pattern == textToScan):
#                 print("found!")
#                 indexArray.append(x)
#             else:
#                 print("Sturious Hit")
#                 sturiousHits += 1
#         # else:
#         #     print("Not found")
#     print(indexArray)
#     print(sturiousHits)


def RKRollingHash(text, pattern, alphabetSize):
    """
    This function takes in 3 arguments:
    1. text -> This is the entire text that is to be scanned
    2. pattern -> The function will be scanning the text for this string
    3. alphabetSize -> This input will be the total number of characters possible present in the text
    """
    patternHash = hashing(
        pattern, alphabetSize)  # Calls the hashing function onto the pattern to generate a hash code for the pattern
    indexArray = []  # This is the array that will store the indexes of all occurences of the pattern in the text
    # This slices the first window of text to be matched with the pattern
    textToScan = text[0:len(pattern)]
    # Calls the hashing function to get its hashcode
    textHash = hashing(textToScan, alphabetSize)
    textLen = len(text)
    patternLen = len(pattern)
    # This multiplier is calculated to aid in the rolling hash, this value along with the character value will be subtracted from the textHash later on
    multiplier = alphabetSize**(patternLen-1)
    for i in range(textLen - patternLen + 1):
        if (patternHash == textHash):
            # If the patternHash matches the textHash, we will need to conduct a naive search on the the strings to see if they match
            for j in range(patternLen):
                if (text[i+j] != pattern[j]):
                    break
            if (j+1 == patternLen):
                indexArray.append(i)

        # This is the rolling hash that calculates the hashcode for the next window in the text
        if (i < textLen-patternLen):
            textHash = (
                textHash - ord(text[i])*multiplier)*alphabetSize + ord(text[i + patternLen])

    print(indexArray)


# path = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001\\ncbi-genomes-2020-09-11\\GCF_000006945.2_ASM694v2_genomic.fna"
# text = next(SeqIO.parse(path, "fasta"))
# print(len(text))
# text = str(text)
# print(len(text))
# pattern = "TGACCTATGAT"
path = "C:\\Users\\user\\Desktop\\Repositories\\CZ2001\\ncbi-genomes-2020-09-11\\GCF_000006945.2_ASM694v2_genomic.fna"
# path = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001\\ncbi-genomes-2020-09-11\\GCF_000006945.2_ASM694v2_genomic.fna"
pattern = "TCTTTCCGGGTCGCTCTCTTTT"
f = open(path, "r")
fileStr = f.read()
f.close()

fileStr = fileStr.split("\n", 1)[1]
text = fileStr.replace("\n", "")
before = time.time()
# # alphabetSize is chosen as 4 here because there are only 4 bases in the genome sequence A,C,T and G
RKRollingHash(text, pattern, alphabetSize=4)
after = time.time()
print(after-before)
