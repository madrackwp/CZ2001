import time
from Bio import SeqIO
import fastaparser


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


path = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001\\ncbi-genomes-2020-09-11\\GCF_000006945.2_ASM694v2_genomic.fna"
pattern = "AAAACCGACGGTC"
f = open(path, "r")
fileStr = f.read()
f.close()

fileStr = fileStr.split("\n", 1)[1]
text = fileStr.replace("\n", "")

# text = open('genomeSequence2.txt', 'r').read().upper()
# text = next(SeqIO.parse(path, "fasta"))
# print(type(text))
# This is the pattern that the algorithm will scan for,
# pattern = "AGAGAT"
# pattern = "DAD"
# print(repr(text.seq))
# with open(path) as fasta_file:
#     parser = fastaparser.Reader(fasta_file)
#     for seq in parser:
#         # seq is a FastaSequence object
#         print('ID:', seq.id)
#         print('Description:', seq.description)
#         print('Sequence:', seq.sequence_as_string())
#         print()


# print(fileStr)
# print(len(fileStr))
before = time.time()
bruteForce(text, pattern)
after = time.time()
print(after-before)
