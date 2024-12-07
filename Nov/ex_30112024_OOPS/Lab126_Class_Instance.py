class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name


Damini = Person("Damini")
Soumya = Person("Soumya")

print(Damini.name)
print(Soumya.name)

print("Who is walking", Damini.walk())
print("Who is walking", Soumya.walk())

"""
Every object has different attribute and behavior.
"""
