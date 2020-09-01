# This will be the text where the algorithm will scan the pattern for
text = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCGCTA"
# This is the pattern that the algorithm will scan for
pattern = "TTTATACCTTCC"
patternMatch = 0
indexLocale = []
indexTemp = 0

for char in text:
    if (char == pattern[patternMatch]):
        if (patternMatch == 0):
            indexTemp = text.index(char)
        patternMatch += 1
    if (patternMatch == len(pattern)):
        print("found!")
        patternMatch = 0
        indexLocale.append(indexTemp)
        indexTemp = None

print(indexLocale)
