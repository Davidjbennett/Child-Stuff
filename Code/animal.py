# animal.py: Illustrates calling superclass constructors

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        print('Animal.__init__')
        self.name = name
    def whoAmI(self):
        return self.name

class SpeakingAnimal(Animal):
    def __init__(self,name):
        print('SpeakingAnimal.__init__')
        super().__init__(name)

    @abstractmethod
    def speak(self):
        pass

class Dog(SpeakingAnimal):
    def __init__(self, name):
        print('Dog.__init__')
        super().__init__(name)
    def speak(self):
        return("Bark!")

class Antelope(Animal):
    def __init__(self, name):
        print('Antelope.__init__')
        super().__init__(name)

d = Dog("Muffy")
a = Antelope("Annie")

animals = [d,a]
for animal in animals:
    print(animal.whoAmI(),end = '')
    speech = ": " + animal.speak() if isinstance(animal,SpeakingAnimal) else ""
    print(speech)

''' Output:
Dog.__init__
SpeakingAnimal.__init__
Animal.__init__
Antelope.__init__
Animal.__init__
Muffy: Bark!
Annie 
'''
