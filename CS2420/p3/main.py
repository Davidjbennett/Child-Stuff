"""Main. Imports csv and reads file. File info is stored in courses in courselist"""
import csv
from course import Course
from courselist import CourseList

def main():
    """reads from data file and creates course objects which are stored in
    the courselist class"""
    course_list = CourseList()
    with open("B:\\GitHub\\HomieRepo\\CS2420\\p3\\data.txt", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for data in reader:
            course = Course(data[0], data[1], data[2], data[3])
            course_list.insert(course)

if __name__ == "__main__":
    main()
