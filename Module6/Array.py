import array

b_array = array.array('b',[2,4,7,15,16,32,64,127]) #b is 1 byte and numbers are in 2s complement
h_array = array.array('h')

for i in b_array:
    print(i)
    h_array.append(i)

h_array.append(32767)
h_array.append(-32768)
print(h_array)
