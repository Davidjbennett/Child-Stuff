"""Class course creates and object course with information
on the course."""
class Course:
    """Course initializer which gives course its various info"""
    def __init__(self, course_num:int = 0, course_name:str = '',
                course_credits:float = 0.0, gpa:float = 0.0):
        self.course_num = int(course_num)
        self.course_name = course_name
        self.course_credits = float(course_credits)
        self.gpa = float(gpa)
        self.next = None
        self.prev = None

    def number(self):
        """returns course number"""
        return int(self.course_num)

    def name(self):
        """returns course name"""
        return self.course_name

    def credit_hr(self):
        """returns course credits"""
        return self.course_credits

    def grade(self):
        """returns gpa"""
        return self.gpa

    def __str__(self):
        """returns toString of course with number, name, credits, and gpa"""
        return ("CS"+str(self.course_num)+" "+self.course_name+" Grade:"+
                str(self.gpa)+" Credit Hours: "+str(self.course_credits))
