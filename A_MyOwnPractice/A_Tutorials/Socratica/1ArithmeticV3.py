#V2 uses 4 types of numbers
#V3 uses 3 types of numbers

#types of numbers: int, float, complex
print("\nNumbers:")
#int
a = 496
print("a(496) is a:",type(a))

#float
e = 2.718281828
f = 2.0
print("e(2.718281828) is a:",type(e))
print("f(2.0) is a:",type(f))

#complex numbers
z = 2 - 6.1j
print("z(2-6.1j) is a:",type(z))


#!
print("\n\nArithmetic:")
#there are 4 operations: + - / * %
x = 28 #int
y = 28.0 #float

print(float(28)) #floats are wider than ints
print(int(3.14)) # ints are narrower than floats

#similarly floats can be made complex, but not vice versa
x = 1.732 + 0j
#print(float(x))

#When combining numbers, python will Widen the type
a = 2 #int
b = 6.0 #float
c = 12 + 0j #complex

#addition
print(a + b) #a will turn to float

#subtraction
print(b - a) #a will become a float

#multiplication
print(a * 7)

#division
print(c / b) #b is widened to complex before division

#modulus
print("Mod:" , 13%5)

print(23/3) #ints return as floats

#You can divide by 0 it will throw an error