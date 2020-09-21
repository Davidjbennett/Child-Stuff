str = "abcdefghijklmnopqrstuvwxyz"

print("Here are some Slices:\n" + str[1:5])
print(str[20:23])
print(str[20])
print(str[-10])
print(str[-20:16])

# str[start:stop:step]
print("\n\nHere are some Strides:\n" + str[0:len(str):3])
print(str[0:15:2])
print(str[0::4])
print(str[-20:len(str):2]) #-20 is the same as starting at 6
print(str[6:len(str):2]) #just to show you ;)
print(str[3:6])
data = "No Way!"
print(len(data))