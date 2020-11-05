import numpy as np

a = np.array(range(10), 'i2')

# print(a)
# print(-a)
# print(a+1)
# print(a.dtype,a.itemsize,a.size,a.nbytes,a.shape)

b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])#adding an extra number to 1 list prints 
                                                     #all list with prefix list
# b_list = []
# for i in b:
#     print(i[0],i[1],i[2])

# print(b, b.shape)
# print(b[1], b[1].shape)
# print(b[0]*b[1])

c = np.array(range(10,20), 'i2')
# print(a)
# print(c)
# print(a*c)

# print(sum(a*c))
# print(np.dot(a,c))
# print(c[3:6])

# c_slice = c[3:6] #points to same location as c
# c_copy = c[3:6].copy() #creates a new location
# c_copy[1] = 14

# print(c_copy)
# print(c)

x = np.arange(18)
print(x)
y = x.reshape(3,3,2)
print(y)
print(np.linspace(0,270,20))