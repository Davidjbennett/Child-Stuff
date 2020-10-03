import math

def f():
    pass #how to tell python to skip this line
#code in the functions is indented

def ping():
    return "Ping" #return returns a values from the string

# print(ping())

# x = "happy"
# print(x)

def sphereVol(r):
    '''Returns the volume of the sphere with radius r''' #a doc string
    vol = (4.0/3.0) * math.pi * r**3 #r**3 is r to the 3rd power
    return vol

def triangleArea(b,h):
    return .5 * b * h

def cm(feet=0, inches=0):
    '''Converts a length from the feet and inches to centimeters'''
    in_to_cm = inches * 2.54
    ft_to_cm = feet * 12 * 2.54
    return ft_to_cm + in_to_cm

# def g(x=0, y):  "x=0 has to go after the non default arguments"
#     pass

def g(y, x=0): #y is a non default argument or a required arguement. You have to have y and not x
    return x+y

print(sphereVol(4), "is the volume of our sphere")
print("The area of our triangle", triangleArea(13.7,12.2))
print("18 inches to cm: ", cm(inches=18), "&", cm(0,18))
print("1.125 inches to cm: ", cm(feet=1.125), "&", cm(1.125,0))
print("1ft 3in", cm(feet=1, inches=3)) #you can flip feet and inches around as long as feet=x and inches=x