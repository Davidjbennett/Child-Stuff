words = [word.upper() for word in open('gettysburg.txt').read().split()]
theDictionary = {}
for word in words:
    theDictionary[word] = theDictionary.get(word,0) + 1
print(theDictionary)
