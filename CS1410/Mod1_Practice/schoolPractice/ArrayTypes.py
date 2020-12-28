#going to talk about tuples, list, dictionaries, etc...

#tuples are immutable meaning they cant be changed. If you want to change
# it you have to create a new one and copy new info into old one. This 
# will create a new variable always

#these are examples of tuples. It uses paranthesis as opposed to brackets
# or curlies braces
fruits = ("banana", "apple", "orange")
numbers = ("13", "73", "87")

#list will use brackets
meats = ['beef', 'poultry', 'seafood']

#you can cast list to tuples
tupMeats = tuple(meats)

#dictionary are used to organize info according to association, not 
#position. These data structures are called 'lookup tables',
#'association list', 'associative arrays', or 'maps'.

#dictionary and sets are best for look up efficiency. Dictionary is stored
#in (key,value) pairs. Cant have duplicate keys in sets or dictionaries

#pairs in a dictionary are sometimes called entries. All entries are 
#enclose in {} and have : in between key & value

phoneBook = {'Tony':'4568942316', 'Vin':'4896521379'}
info = {}
info["name"] = "Stan"
info["occupation"] = "hacker"

print(info)

#can change keys
info["occupation"] = "manager"
print(info)

#must pass in the key, not just a number. If the key isnt there you 
#get an error
print(info["name"])
#this is the error code => print(info["butt"])

#you can check for key by doing: printing to show output
print("job" in info)
print(info.get('occupation', 'Job not in dictionary'))
print(info.get('singing', 'Job not in dictionary'))

print(info.setdefault('occupation', 'value not there'))

#removing keys from dictionary
print(info.pop("occupation"))
print("occupation" in info)

#can trverse a dictionary by:
for key in info:
    print(key, info[key])

#entries are represented as tuples in list
grades = {90:'A', 80:'B', 70:'C'}
list(grades.items())
for key, value in grades.items():
    print(key, value)

theKeys = list(info.keys())
theKeys.sort()
for key in theKeys:
    print(key, info[key])

