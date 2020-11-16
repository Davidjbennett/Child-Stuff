
#!TimeStamp: 3pm to 430 pm

# f = open("booklist.txt", "r")
# list = []
# for line in f:
#     list.append(line.strip().split(','))
#     print(line)

# # for line in list:
# #     print(line) #prints ['John Wyndham', 'The Chrysalids']
# #     print(line[0] + ", " + line[1]) # prints John Wyndham, The Chrysalids
#!------------------------------------------------------------------------------
#! ^^^OLD ---NEW BELOW

# f = open("booklist.txt", "r")
# list = []
# for line in f:
#     # list.append(line.strip().split(',')[0] + ", " + line.strip().split(',')[1])
#     # ^^^ doesnt work.. prints a bunch of list
#     list.append(line.strip().split(','))

# for line in list:
#     print(line[0]+", "+line[1])
#!Have to creat 2 for loops as i know. to append and then print the proper list

# readRatings = open("ratings.txt","r")
# count = 1
# name = "name"
# ratingsList = []
# numList = []
# for line in readRatings:
#     if count % 2 != 0:
#         name = line.strip().lower() + "!"
#         # print(name) #prints name with a !
#     else:
#         numList = line.split()
#         numberList = []
#         for l in numList:
#             l = int(l)
#             numberList.append(l)
#         # numList.append(line.strip()) #prints numbers without newlines
#         ratingsDic = {"name": name, "ratings": numberList}
#         ratingsList.append(ratingsDic)
#     count+=1

# # print(numList) #prints the rating numbers
# # print(numberList[1])
# # print(ratingsList) ratingsList is a list with a dictionary inside

# # a = []
# # s = "This is a string"
# # for l in s:
# #     a.append(s.split(" "))
# # print(a) 
#! elements are found in a list not a string.. thats why we make 
#! numList a list before we do a for loop on it
#!----------------------------------------------------------------------------------
#! ^^^OLD NEW BELOW:


r = open("booklist.txt","r")
# print(r.readline()) only reads 1 line
#!pretty sure you can only read a whole file with a for loop

import os
# # r = open("afile", "x")
# os.remove("afile") removes a file from the system
# os.rmdir("afile") removes a directory
