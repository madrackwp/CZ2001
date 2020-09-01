text = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCGCTA"
pattern = "TTTATACCTTCC"
patternMatch = 0
indexLocale = [None]
indexTemp = None

for index in text:
    if (index == pattern[patternMatch]):
        if (patternMatch == 0):
            indexTemp = text.index
        patternMatch += 1
    if (patternMatch == len(pattern)):
        print("found!")
        patternMatch = 0
        indexLocale.append(indexTemp)
    indexTemp = None

print(indexLocale)
