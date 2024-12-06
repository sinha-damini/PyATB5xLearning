# Take input and create a class in python

class Person:

    def __init__(self):
        print("I will be called")
        self.name = input("Enter the name\n")
        self.age = input("Enter your age\n")
        self.phone = input("Enter your phone\n")
        self.occupation = input("Enter your occupation\n")

    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}", f"Age is {self.age}", f"Phone is {self.phone}",
              f"occupation is {self.occupation}")


person1 = Person()
person1.name_of_the_function_to_display()


"""
This constructor:

Has no parameters apart from self.
The required attributes (name, age, phone, occupation) are fetched through user input.
If the constructor accepted parameters like def __init__(self, name, age, phone, occupation):, 
it would be a parameterized constructor.

"""
print("<<<<<  Code with Parameterized Constructor (for comparison): >>>>>>>")
class Person:
    def __init__(self, name, age, phone, occupation):
        self.name = name
        self.age = age
        self.phone = phone
        self.occupation = occupation

    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}", f"Age is {self.age}", f"Phone is {self.phone}",
              f"Occupation is {self.occupation}")

person1 = Person("Alice", 30, "1234567890", "Engineer")
person1.name_of_the_function_to_display()