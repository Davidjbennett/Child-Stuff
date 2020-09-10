alpha = "abcdefghijklmnopqrstuvwxyz"

with open("WriteFile.txt", 'w') as f: # 'a+' in place of 'w' opens 
    i = 0                             #file without deleting insides
    aLength = len(alpha)
    while i < aLength:
        f.write(alpha[i:aLength] + "\n")
        i += 1
        aLength -= 1

pass

# #to write two lines of text
# f = open("WriteFile2.txt", 'w') 
#have to close file when calling it this way ^^
# f.write("Check it out.\n Hey bb\n")       
# this line and the lower line both write to the file^^
# print("Check it out.\n Hey bb\n", file=f)
# f.close()
# 
# #Will not create a file if not there when trying to read one
# with open("WriteFile.txt", 'r') as f: #file automatically closed this way
# when opened this way it also returns a list of lines
#     if(not f):
#         print("File does not exist")
#     else:
#         lines = f.readlines() # returns \n in stream as well
#         print(lines)
#         
# with open("WriteFile2.txt", 'r') as f:
#     for line in f:
#         print(line.rstrip())
# 
# with open("WriteFile2.txt", 'r') as f:
#     while True:
#         line = f.readlines().strip()
#         if line == "":
#             break
#         print(line)

# with open("WriteFile2.txt", 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip())

try:
    with open("noExist.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
except:
    print("Unable to open file noExist.txt")


# list1 = [1,2,3]
# list2 = ['a', 'b', 'c']
# list3 = [7,8,9]
# 
# #listNew = list(zip(list1, list2, list3))
# #print(listNew)
# 
# for list1, list2 in zip(list1, list2):
#     print(list1, list2, sep=', ', end=' |\n')

with open("myFile.txt", 'w') as f:
    for i in range(10):
        #f.write(str(i)) #wont take int so have to cast to string
        print(i, file=f)

with open("myFile.txt", 'r') as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        total += int(line)