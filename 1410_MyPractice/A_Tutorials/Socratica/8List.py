example = list([1,2,3]) #two ways to make list
primes = [2,3,5,7,11,13]
primes.append(17)
primes.append(19)

# for i in example:
#     print(i)

#! list preserve order
print(primes[0])
print(primes[3])
print(primes[-1])

print(primes[2:5:2]) #! [Start:Stop:Increase Index by]

#You can insert multiple data types into list

rolls = [4,2,7,2,7,12,4,7] #!will include repeats
numbers =[1,2,3]
letters = ['a','b','c']

print(numbers + letters) #order matters here
print(letters + numbers)

primes.reverse()
print(primes) #cant reverse the list in the print statement