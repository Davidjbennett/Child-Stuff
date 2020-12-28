import math
from abc import ABC, abstractmethod

class Shape():
    def __init__(self, name):
        pass

    @abstractmethod
    def getName(self):
        pass
    
    @abstractmethod #decorator
    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        # shape.__init__(self, "Rectangle")
        super().__init__("Rectangle")

        self.length = length
        self.width = width
    
    @abstractmethod
    def getArea(self):
        return self.length * self.width

    def getName(self):
        return "Rectangle"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")

        self.radius = radius

    def getArea(self):
        return math.pi * (self.radius ** 2)
    
    def getName(self):
         return "Circle"

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.name = "Triangle"
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getArea(self):
        s = (self.side1 +self.side2 + self.side3) / 2
        return math.sqrt(s*(s - self.side1)*
                        (s - self.side2)*
                        (s - self.side3))
    
    def getName(self):
         return "Triangle"
    
    def newSides(self, s1, s2, s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

# class Monkey():
#     def __init__(self):
#         pass
    
#     def getName(self):
#          return "im a monkey"

# def addShape(lyst, shape):
#     if isinstance(shape, Shape):
#         print(shape.getName(), "is a shape.")
#         return
#     else:
#         print(str(shape), "is not a shape")
#     lyst.append(shape)

lyst = []
r = Rectangle(10,4)
c = Circle(90)
t = Triangle(5, 8, 12)
# addShape(lyst, r)
# addShape(lyst, c)
# addShape(lyst, t)



def main():
    print(t.getArea())
    t.newSides(52,65,34)
    print(t.getArea())
    # for shape in lyst:
    #     print(shape.getArea() + ":")
    #     print(shape.getName(), shape.getArea())

if __name__ == "__main__":
    main()