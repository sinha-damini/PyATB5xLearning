class Father:
    def home(self):
        print("1BHK")

class Pramod(Father):
    def home(self):
        print("3BHK")


p = Pramod()
p.home()

# f = Father()
# f.home()

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

c = Dog()
print(c.sound())  # Output: "Bark"

p = Animal()
print(p.sound())  # Output: "Some sound"