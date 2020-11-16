
# input = input("Please enter a test string:") #collect input from user

# if len(input) < 6:
#     print("Your string is too short")
#     print("Please enter a string with at least 6 characters")



# input = input("Please enter an integer: ")
# number = int(input)

# if number % 2 == 0:
#     print("Your number is even")
# else:
#     print("Your number is odd")



a = int(input("Length of side a: "))
b = int(input("Length of side b: "))
c = int(input("Length of side c: "))

if a != b and b != c and a != c:
    print("This is a scalene triangle")
elif a ==b and b == c:
    print("This is an equalateral triangle")
else:
    print("This is a isosceles triangle")
