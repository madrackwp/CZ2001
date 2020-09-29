def boyersMoore(text, pattern):
    indexList = []
    badMatchTable = genBadMatchTable(pattern)
    n = len(pattern)
    m = len(text)

    for i in range(n-1,m): #REPLACE FOR LOOP WITH A WHILE LOOP!
        firstLetter = text[i] #First letter from the back
        # print(firstLetter)
        for j in range(n): #This loop is to check through the pattern and the text
            if pattern[n-1-j] == text[i-j]: 
                continue
                # print("hello")
            else: #We are looking at the first mismatched char in the text! So we need a way to keep track
                mismatchedChar = text[i]
                value = badMatchTable.get(mismatchedChar) if badMatchTable.get(mismatchedChar)!=None else n
                i+=value
                break
            if j == n-1:
                indexList.append(i)
    print(indexList)



def genBadMatchTable(text):
    m = len(text)
    badMatchTable = {}
    for index in range(m):
        char = text[index]
        value = m - index -1
        if badMatchTable.get(char) != None: #When the table does not contain that char
            badMatchTable[char] = value
        else: 
            badMatchTable[char] = value 
    #Last char will always have the value as the length of the text
    badMatchTable[text[-1]] = m
    return badMatchTable


text = "WELCOMETOSURANACOLLEGE"
pattern = "COLLEGE"

boyersMoore(text, pattern)
