class helloWorld():
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def getLen(self):
        return self.length

    def getWid(self):
        return self.width
    
    def __str__(self):
        return f"Length:{self.length} Width:{self.width}"

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Ruff")

def main():
    a = helloWorld(10,5)
    b = helloWorld(3,7)
    c = helloWorld(2,8)

    dog1 = Dog('Ruby', 3)
    dog2 = Dog('Tank', 1)

    print(self.a)
    print(a)

if __name__ == "__main__":
    main()

    #! self is instance variables. The scope is within the class