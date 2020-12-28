import sys
import timeit

# prime_numbers = [2,3,5,7,11,13,17] #heres a list
# perfect_squares = (1,4,9,16,25,36)    #heres a tuple

# print("Primes", len(prime_numbers))
# print("Squares", len(perfect_squares))

# for p in prime_numbers:
#     print("Prime", p)

# for n in perfect_squares:
#     print("Squares", n)

#! list have more functions to use than tuples but require more memory

# print(dir(sys))
# print(help(sys.getsizeof))
# list = [1,2,3,4,5]
# tuple = (1,2,3,4,5)

# print("Size of same group of numbers as List", sys.getsizeof(list))
# print("Size of same group of numbers as Tuple", sys.getsizeof(tuple))

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)

print("List time", list_test)
print("Tuple time", tuple_test)

empty=()
test1 = ('a')
test2 = ('a','b')

print(empty)
print(test1) #single value tuple will print value only not brackets. must add, at the end
print(test2)

#heres another way of making a tuple. Dont need ()
testa=1, #a comma at the end will make it a tuple
testb=1,2