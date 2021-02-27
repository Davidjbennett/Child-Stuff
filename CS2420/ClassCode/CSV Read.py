import csv

class Book:
    def __init__(self, title, author, genre, length, publisher):
        self.title = title
        self.author = author
        self.genre = genre
        self.length = length
        self.publisher = publisher
        
    def __str__(self):
        return f"Title:{self.title}, Author:{self.author}, Genre: {self.genre}"

class Course:
    def __init__(self, course_num:str, course_name:str, 
                 course_credits:int, gpa:float):
        self.course_num = course_num
        self.course_name = course_name
        self.course_credits = course_credits
        self.gpa = gpa

    def number(self):
        return int(self.course_num)

    def name(self):
        return self.course_name

    def credit_hr(self):
        return self.course_credits

    def grade(self):
        return self.gpa

    def __str__(self):
        return f"CS{self.course_num} {self.course_name} Grade:{self.gpa} Credit Hours: {float(self.course_credits):.1f}"


def LoadBooks():
    books = []
    with open("D:\\UVU\\Spring 2021\\CS2420\\data.txt", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            if line_count > 0:
                books.append(Course(row[0], row[1], row[2], row[3]))
            line_count += 1
    
    return books

mybooks = LoadBooks()
for book in mybooks:
    print(book)
