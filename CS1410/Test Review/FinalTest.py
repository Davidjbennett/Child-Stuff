
# m = [[x,x+2,x+1] for x in range(1,9,3)]
# print(m)

# points = [[1, 2], [3, 1.5], [0.5, 0.5]]
# points.sort()
# print(points)

# x = 1
# def f1():
#     x = x + 2
#     print(x)

# f1()
# print(x)

# def f1(x = 1, y = 2):
#     return x + y, x - y

# x, y = f1(y = 2, x = 1)
# print(x, y)

# x = 1
# def f1():
#     global x
#     x = x + 2
#     print(x, end=' ')

# f1()
# print(x) 

# def f(value, values):
#     v = 1
#     values[0] = 44

# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])

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

class A:
    def __init__(self):
        self.setI(10)

    def setI(self, i):
        self.i = 2 * i;

class B(A):
    def __init__(self):
        super().__init__()
        print("i from B is", self.i)
        
    def setI(self, i):
        self.i = 3 * i;

b = B()