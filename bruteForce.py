text = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCGCTA"
pattern = "TTTATACCTTCC"
patternMatch = 0
indexLocale = null

for index in text:
    if (index == pattern[patternMatch]):
        patternMatch += 1
    if (patternMatch == len(pattern)):
        print("found!")
        patternMatch = 0
