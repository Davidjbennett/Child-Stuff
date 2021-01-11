
#!time stamp: 3:45pm to 5:00pm

#when using dict method you dont have to use quotes for keys, but must use an equal
#between key and value
pizza = dict(dough="Slightly sweet", tomatoSauce="medium", cheese="Heavy", 
            pepperoni="Heavy" )

#can update a dictionary with a new dictionary. Dictionaries can hold list and tuples
pizza.update({"pepperoni": "A lot", "condiments": ["Olives", "chicken", "bacon"]})
#del is a keyword that deletes specified
del pizza["tomatoSauce"]

# for key in pizza.keys():
#     print(str(key) + ":", pizza[key])

#!Cant figure out why line in second para is printing different than this 1st one
#!Why does this one read the author and then the book title? makes it into seperate
#!things within the tuple
# with open("booklist.txt", 'r') as f:
#     pass
#     books = []
#     for line in f:
#         books.append(tuple(line.strip().split(',')))
#         # print(line)
#     print(books)

# tup = "Douglas Adams The Hitchhiker's Guide To The Galaxy"
# for line in tup:
#     print(line)

# for i in range(10):
#     print(i);print("Yo")

#for i in range(10): print(i**2 if i<5 else 0)

squares = [i**2 for i in range(10)]
print(squares)



