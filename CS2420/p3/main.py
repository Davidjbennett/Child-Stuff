from course import *
import csv
from courselist import *

def main():
    book_list = CourseList()
    with open("D:\\UVU\\Spring 2021\\CS2420\\data.txt", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for data in reader:
            book = Course(data[0], data[1], data[2], data[3])
            book_list.insert(book)
    
   #!Prints a 1030 then none on the line below
    print(book_list.info())

    #!Only prints a pointer
    a = book_list.find(1400)
    print(a)

    #! 1030 is not removed from the list
    book_list.remove(1030)
    print(book_list)


if __name__ == "__main__":
    main()
