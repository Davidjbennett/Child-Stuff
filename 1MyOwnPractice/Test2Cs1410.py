# class A:
#      def  __init__(self,  s = "welcome"):
#          self.s = s
 
#      def print(self):
#          print(self.s)

# a = A()
# a.print()

# def main():
#     myCount = Count()
#     times = 0

#     for i in range(0, 100):
#         increment(myCount, times)

#     print("myCount.count =", myCount.count, "times =", times)

# def increment(c, times):
#     c.count += 1
#     times += 1

# class Count:
#     def __init__(self):
#         self.count = 0
    
# main()

# class A:
#     def __init__(self, i = 0):
#         self.i = i

# class B(A):
#     def __init__(self, j = 0):
#         self.j = j

# b = B()
# print(b.i)
# print(b.j)

# class A:
#     def __init__(self, i = 1):
#         self.i = i

# class B(A):
#     def __init__(self, j = 2):
#         super().__init__()
#         self.j = j

# def main():
#     b = B()
#     print(b.i, b.j)

# main()

# class A:
#     def __init__(self):
#         self.i = 1

#     def m(self):
#         self.i = 10

# class B(A):
#     def m(self):
#         self.i += 1
#         return self.i


# def main():
#     b = B()
#     print(b.m())

# main()

# class A:
#     def __str__(self):
#         return "A"

# class B(A):
#     def __init__(self):
#         super().__init__()

# class C(B):
#     def __init__(self):
#         super().__init__()

# def main():
#     b = B()
#     a = A()
#     c = C()
#     print(a, b, c)

# main()

# class A:
#     def __init__(self, i = 2, j = 3):
#         self.i = i
#         self.j = j

#     def __str__(self):
#         return "A"

#     def __eq__(self, other):
#         return self.i * self.j == other.i * other.j

# def main():
#     x = A(1, 2)
#     y = A(2, 1)
#     print(x == y)

# main()

# class A:
#     def __init__(self):
#         self.setI(20)

#     def setI(self, i):
#         self.i = 2 * i;

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("i from B is", self.i)
        
#     def setI(self, i):
#         self.i = 3 * i;


# b = B()