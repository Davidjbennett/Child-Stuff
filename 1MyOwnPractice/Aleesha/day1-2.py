
import math

#comments

#variables:
intt = 6
intt2 = 7
floatt = 1.1
address = "3124 e sioux st"
David = True
count = 0

# if intt == 5:
#     print("im less than 7")
# elif intt > 7:
#     print("grreater")
# else:
#     print("yoyoy")

# if David == True:
#     print("Hes the best")
#     print(David + David)

tup = ("David", "Aleesha", "Jimmy", "Susie")
lis = ["David", "Aleesha", "Jimmy", "Susie"]
# dic = {key:value}
dic = {'Food':'Watermelon'}

lis.append("Jack")
# lis.reverse()
# print(lis)

# for a in lis:
#     print(a)

# while David == True:
#     print("Wow")
#     count +=1
#     if count == 5:
#         David = False

def circle_Area(radius):
    return math.pi * (radius**2)

def main():
    print(circle_Area(6))
    print(circle_Area(7))
    print(circle_Area(4))
    print(circle_Area(3))

if __name__ == "__main__":
    main()





