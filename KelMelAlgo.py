import time

# with open('Human.txt', 'r') as file:
#     data = file.read().replace('\n', '')

path = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001\\ncbi-genomes-2020-09-11\\GCF_000006945.2_ASM694v2_genomic.fna"
pattern = "AAAACCGACGGTC"
f = open(path, "r")
fileStr = f.read()
f.close()

fileStr = fileStr.split("\n", 1)[1]
text = fileStr.replace("\n", "")

foundindex = []
foundtrueindex = []

def compile(data): 
    newString = ""
    counter = 1
    prevChar=''
    for index in range(0,len(data),1):
        if(data[index] != prevChar):
            if(index != 0):
                newString = newString+ prevChar+ str(counter)
                counter = 1
        else:
            counter += 1

        if(index == len(data)-1):
            newString = newString+ data[index]+ str(counter)
        
        prevChar = data[index]

    return newString

# subsetStr = ""
# subsetStr = str(input("Enter a Sequence: ")).upper()



def search(compiledData,compiledSubsetStr):
    mainindex=0
    substrindex=0
    trueindex = 0

    for mainindex in range(0,(len(compiledData)-len(compiledSubsetStr)+1)):
        if(mainindex % 2 == 1):
            trueindex+=int(compiledData[mainindex])
        for substrindex in range(0, len(compiledSubsetStr)):

            if(substrindex == 1 or substrindex == len(compiledSubsetStr)-1):
                if(int(compiledData[mainindex+substrindex]) < int(compiledSubsetStr[substrindex])):
                    break
            else:
                if(compiledData[mainindex+substrindex] != compiledSubsetStr[substrindex]):
                    break
            if(substrindex == len(compiledSubsetStr)-1):
                if(int(compiledData[mainindex+1]) > int(compiledSubsetStr[1])):
                    tempIndex = trueindex
                    tempIndex += (int(compiledData[mainindex+1]) - int(compiledSubsetStr[1]))
                    foundtrueindex.append(tempIndex)
                else:
                    foundindex.append(mainindex+1)
                    foundtrueindex.append(trueindex)


before = time.time()
compiledData = compile(text)
compiledSubsetStr = compile(pattern) 
search(compiledData,compiledSubsetStr)
print(foundtrueindex)
after = time.time()
print(before-after)