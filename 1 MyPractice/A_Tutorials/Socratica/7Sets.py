example = set()

example.add(42)
example.add(False)
example.add(3.13159)
example.add("Thorium")

print(example)
example.add(42) #doesnt add an extra 42
print(example)
print(len(example))

example.remove(42) #if you specify a number not in the set, it will give an error
print("Removed 42 before this", example, "\n")

#print(help(example.discard)) how to print a specific functions doc string

example.discard(50) #doesnt give an error if the element is not in the set, unlike remove

example0 = [28, True, 2.71828, "Helium"] #this is a list
example2 = set([28, True, 2.71828, "Helium"]) #this is a set and theyre different

print(len(example2)) #returns 4
example2.clear()
print(len(example2)) #returns 0

odds = set([1,3,5,7,9])
evens = set([0,2,4,6,8])
primes = set([2,3,5,7])
composites = set([4,6,8,9])

print(odds.union(evens))
print(evens.union(odds))
print(odds)
print(evens)
print(odds.intersection(primes))
print(evens.intersection(primes))
print(6 in evens)
print(9 not in evens)