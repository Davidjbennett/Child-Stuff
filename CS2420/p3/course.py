class Course:
    def __init__(self, course_num:str, course_name:str, 
                 course_credits:int, gpa:float):
        self.course_num = int(course_num)
        self.course_name = course_name
        self.course_credits = course_credits
        self.gpa = gpa

    def number(self):
        return self.course_num

    def name(self):
        return self.course_name

    def credit_hr(self):
        return self.course_credits

    def grade(self):
        return self.gpa

    def __str__(self):
        return f"CS{self.course_num} {self.course_name} Grade:{self.gpa} Credit Hours: {float(self.course_credits):.1f}"
