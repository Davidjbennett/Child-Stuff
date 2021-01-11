print(True) 
print(False, "\n\n") #booleans have to be capitalized or they return false

a =3
b =5
print(a==b) #a is equal to b equal False
print(a!=b) #a is not equal to b equal True
print(a<b) #less than
print(a>b, "\n") #greater than

print(bool(28))
print(bool(-2.1562))
print(bool(0), "\n")

#with strings, trivial values are false and vice versa
print(bool('turing'))
print(bool(' '))
print(bool(''), "\n") 

print(str(True))
print(str(False), "\n")

print(int(True)) #1 is true and 0 is false
print(int(False))
print(10 * False)