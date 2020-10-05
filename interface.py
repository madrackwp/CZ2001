from boyersMoore import boyersMoore
from KMP import KMPAlgo
from bruteForce import bruteForce
import time




#==================================EDIT THIS ONLY AND NOTHING ELSE=============================================
PATH = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001\\DNASequences\  \GCF_000006945.2_ASM694v2_genomic.fna"
#==============================================================================================================

pattern = "TCTTTCCGGGTCGCTCTCTTTT"
f = open(PATH, "r")
fileStr = f.read()
f.close()
fileStr = fileStr.split("\n", 1)[1]
text = fileStr.replace("\n", "")


while True:
    print("=========================DNA SEQUENCE SEARCHER=========================")
    patternSelector = input("Select 1 for inbuilt pattern, 2 for custom pattern\n")
    if (int(patternSelector) == 1):
        pattern = "TCTTTCCGGGTCGCTCTCTTTT"
        print("Inbuilt pattern = TCTTTCCGGGTCGCTCTCTTTT")
    elif (int(patternSelector) == 2):
        pattern = input("Please select the pattern to be searched for (ACTG Only)\n").upper()
        print(f"Custom pattern = {pattern}")
    else:
        pattern = None
        print("Enter a proper input!")
    
    if (pattern != None):
        print("==========================================================================")
        print("=======================CHOOSE YOUR ALGORITHM==============================")
        print("==========================================================================")
        userInput = input("Select 1 for bruteforce, 2 for KMP, 3 for Boyers Moore, 4 to quit\n")
        indexArray=None
        if (int(userInput) == 4):
            print("Goodbye!")
            break
        elif (int(userInput) == 1):
            before = time.time()
            indexArray = bruteForce(text,pattern)
            after = time.time()
            duration = after - before
            print(f"\nTime taken: {duration}s")
        elif (int(userInput) == 2):
            before = time.time()
            indexArray = KMPAlgo(text, pattern)
            after = time.time()
            duration = after - before
            print(f"\nTime taken: {duration}s")
        elif (int(userInput) == 3):
            before = time.time()
            indexArray = boyersMoore(text, pattern)
            after = time.time()
            duration = after - before
            print(f"\nTime taken: {duration}s")
        else:
            print("Please enter a valid input!")

        if (indexArray == None):
            print("Patter not found!")
        else:
            print(indexArray)

