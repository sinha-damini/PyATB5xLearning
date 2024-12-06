# Constructor - parameterized


class Student:
    # Constructor - parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name
    def show(self):
        print("Hello",self.name)
student = Student("John")
student.show()

print("<<<<<<<<<<<<<<<<<<< 2nd Example >>>>>>>>>>>>>>>>>>>>>>>>>")

class Dog:
    # Attributes - Instance variables | Data variables
    name = None
    breed = None
    height = None
    weight = None
    race = None


    def __init__(self, name, breed):
        print("PC")
        self.name = name
        self.breed = breed

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is sleep -> " + self.name )

    def talk(self):
        pass


# Object Ref
chow_ref = Dog("chow","pitbull")
print(chow_ref.name)
chow_ref.bark()
chow_ref.sleep()
print(id(chow_ref)) #gives the address.


mow_ref = Dog("mow","husky")
print(mow_ref.name)
mow_ref.sleep()
print(id(mow_ref))