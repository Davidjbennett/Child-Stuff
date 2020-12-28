
#! Test has 25 questions. All multiple choice. 

#!first thing to know. How to create list
list = [1,2,3]

#! slices and strides
s = "hello world"
print(s[2:8]) #[start:stop:increment] will default at 0 if not input
print(s[::2])

#! list comprehensions (inline for loop)
lyst = [2 ** x for x in range(1,11)]
print(lyst)
lyst1 = [(3 + x)*5 for x in [2,5,6,8,7,3]]
print(lyst1)

#! truthiness. The following are falsy (considered False in a condition)
# Everything else is truthy
if 0:
    print(0)
if "":
    print("")
if None:
    print(None)
if []:
    print([])
if {}:
    print({})
if ():
    print(())

#remember this one for the test
if [""]:
    print(["omg it worked!"])

#! Aliasing and Side Effects
first = [10,20,30]
second = first #We set second to be an ALIAS here. 
               #They refer to the exact same list object.
print(first)
print(second)
first[1] = 99
print(first)
print(second)
third = first.copy()
first[1] = 100
print(first)
print(second)
print(third) #gets a copy of the list object and makes a new one

#! Tuples
#tuples are immutable
str = ("here", "ya","go", "mate")

#!Reading and writing to a file
#if you open a file for reading that doesnt exist you get an error
#if you do the same but for a writing file, it will create one
#when writing if the file exist, it truncates it

#! Sets
#like dictionary but there are no values, just keys
#no duplicates allowed (like dictionaries)
#supports set operations like union, intersection, difference, etc...
x = set(['a','b','c','f'])
y = set(['d','e','f','c'])

print(y.difference(x))

#! functions
k=2
def dosomething(x, list):
    x+=4
    list[3] = 99

dosomething(k, lyst) #ints, char, etc. are passed in by copy
print(k, lyst) #objects are passed in by reference

#! Using keywords for default and optional arguments
#when declaring a funcation you can have required and optional arguements
#required arguements always come first

def f(a,b,c,e=4,f=5):
    pass

# def f(a=3,b,c,e=4,f=5): a=3 must come after required arguments
#     pass


#! Scope (2/3), OOPS, Fixed
x=5
def f():
    x=10

f()
print(x) #returns the global x, not the one from the function

def f1():
    global x
    x=10

f1() #changes x to 10 bc global x is called in the function
print(x)

# def oops():
#     x = x + 1   x in x+1 is not assigned yet
# oops()

# def fixed():
#     global x
#     x = x + 1
# fixed()

#!

# def xfunction(x,length):
#     print(x[length-1], end = " ")
#     xfunction(x, length-1)

# xfunction(lyst, len(lyst))

#! Sorted by an embedded Key


#! Returns
#anytime a function doesnt explicitally return something, it will return none


#! Accessing Values
info = {"name":"Sandy", "occupation":"hacker"}
print(info["name"])
print(info.get("name", "doesnt have a name"))
print(info.get("job", "what job?"))

