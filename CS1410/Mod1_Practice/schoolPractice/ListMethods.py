from operator import itemgetter

# myList = [1,2,3]
# myList.append(4)
# myList.extend([6,7,8])
# myList.insert(4,5)
# print(myList)
# print(myList.pop())
# print(myList)
# print(myList.pop(4))
# print(myList)
# 
# aList = [34,45,67]
# for n in (45,50):
#     if n in aList:
#         print(f"{n} is in position, {aList.index(n)}")
#     else:
#         print(f"{n} is not in the list")
# 
# unsortedList = [23,1,45,3,56,2,12]
# sortedList = unsortedList.sort()
# print(sortedList)
# unsortedList.sort()
# print(unsortedList)

words = "now now is the time for all good men to come to the aid of their country".split()
word_counts={}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

def by_count(pair):
    return pair[1]

items = list(word_counts.items())
print(items)
print(sorted(items, key=by_count))
print(sorted(items, key=operator.itemgetter(1)))
print(sorted(items, key=operator.itemgetter(1), reverse=True))

def by_count_word(pair):
    return (pair[1], pair[0])

print(sorted(items, key=by_count_word))
print(sorted(items, key=operator.itemgetter(1,0)))




