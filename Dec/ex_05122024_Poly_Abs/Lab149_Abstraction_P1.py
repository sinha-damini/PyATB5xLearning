from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        print("It can make sound.")
        pass

class Dog(Animal):
    def make_sound(self):
        print("Barking.")

dog_ref = Dog("Candy")
dog_ref.make_sound()