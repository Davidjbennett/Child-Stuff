class A():
    def __init__(self):
        pass
    def f(self):
        return "A"
    

class B(A):
    def __init__(self):
        pass
    def f(self):
        return "B"
    def g(self):
        return "B"

class C(B):
    def __init__(self):
        pass
    def g(self):
        return "C"

class D(C):
    def __init__(self):
        pass

d = D()
print(d.f())
print(d.g())