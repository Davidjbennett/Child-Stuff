from abc import ABC, abstractmethod
import math

# This version has serial object IDs obtained in the constructors.
# Illustrates static data and methods.
# Also provides a __str__ method for each concrete class.

class Shape(ABC):
    id = 1
    @abstractmethod
    def area(self):
        pass        # No body

    @staticmethod
    def getID():    # No "self"
        thisID = Shape.id
        Shape.id += 1
        return thisID

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        self.id = Shape.getID()
    def area(self):
        print('Calling Circle.area')
        return math.pi*self.radius**2
    def __str__(self):
        return "Circle #" + str(self.id) + ", radius = " + str(self.radius)

class Rectangle(Shape): 
    def __init__(self,length,width):
        self.length,self.width = length,width
        self.id = Shape.getID()
    def area(self):
        print('Calling Rectangle.area')
        return self.length*self.width
    def __str__(self):
        return "Rectangle #" + str(self.id) + ", length = " + str(self.length)  + \
               ", width = " + str(self.width)

class Triangle(Shape): 
    def __init__(self,side1,side2,side3):
        self.side1,self.side2,self.side3 = side1,side2,side3
        self.id = Shape.getID()
    def area(self):
        print('Calling Triangle.area')
        # Heron's Formula:
        s1,s2,s3 = self.side1,self.side2,self.side3
        p = (s1+s2+s3)/2
        return math.sqrt(p*(p-s1)*(p-s2)*(p-s3))
    def __str__(self):
        return "Triangle #" + str(self.id) + ", with sides "  + "(" + str(self.side1) \
               + "," + str(self.side2) + "," + str(self.side3) + ")"

def main():
    c = Circle(3)
    r = Rectangle(12,35)
    t = Triangle(3,4,5)
    shapes = [c,r,t]
    for shape in shapes:
        print(shape,"area =",shape.area())

if __name__ == '__main__':
    main()

''' Output:
Calling Circle.area
Circle #1, radius = 3 area = 28.274333882308138
Calling Rectangle.area
Rectangle #2, length = 12, width = 35 area = 420
Calling Triangle.area
Triangle #3, with sides (3,4,5) area = 6.0
'''
