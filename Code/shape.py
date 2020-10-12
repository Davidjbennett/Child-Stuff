from abc import ABC, abstractmethod
import math

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass		# No body

class Circle(Shape):
	def __init__(self,radius):
		self.radius = radius
	def area(self):
		print('Calling Circle.area')
		return math.pi*self.radius**2

class Rectangle(Shape): 
	def __init__(self,length,width):
		self.length,self.width = length,width
	def area(self):
		print('Calling Rectangle.area')
		return self.length*self.width

class Triangle(Shape): 
	def __init__(self,side1,side2,side3):
		self.side1,self.side2,self.side3 = side1,side2,side3
	def area(self):
		print('Calling Triangle.area')
		# Heron's Formula:
		s1,s2,s3 = self.side1,self.side2,self.side3
		p = (s1+s2+s3)/2
		return math.sqrt(p*(p-s1)*(p-s2)*(p-s3))

def main():
	c = Circle(3)
	r = Rectangle(12,35)
	t = Triangle(3,4,5)
	shapes = [c,r,t]
	for shape in shapes:
		print(shape.area())

if __name__ == '__main__':
	main()

''' Output:
Calling Circle.area
28.274333882308138
Calling Rectangle.area
420
Calling Triangle.area
6.0
'''
