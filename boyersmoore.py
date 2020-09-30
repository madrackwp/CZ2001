def boyersMoore(text, pattern):
    indexList = []
    badMatchTable = genBadMatchTable(pattern)
    n = len(pattern)
    m = len(text)

    i = n-1
    while i<m:   
        badMatch = False

        for j in range(n): #This loop is to check through the pattern and the text
            if pattern[n-1-j] == text[i-j]: 
                pass
            else: #We are looking at the first mismatched char in the text! So we need a way to keep track
                badMatch = True
                mismatchedChar = text[i]
                value = badMatchTable.get(mismatchedChar) if badMatchTable.get(mismatchedChar)!=None else n
                i+=value
                break
            if j == n-1: 
                indexList.append(i-n+2)
        if badMatch==False: #This is the iterator when it is not a mismatch
            i+=1
    if (indexList):
        print(indexList)
    else:
        print("No matches found!")


def genBadMatchTable(text):
    m = len(text)
    badMatchTable = {}
    for index in range(m):
        char = text[index]
        value = m - index -1
        if index == m-1:
            pass
        else:
            if badMatchTable.get(char) != None: #When the table does not contain that char
                badMatchTable[char] = value
            else: 
                badMatchTable[char] = value 
    return badMatchTable


