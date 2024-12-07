class Student:
    def __init__(self, name, roll_number):
        self.name = name  # Public attribute
        self.__roll_number = roll_number  # Private attribute


    def get_roll_number(self):
        return self.__roll_number


    def set_roll_number(self, roll_number):
        if isinstance(roll_number, int) and roll_number > 0:
            self.__roll_number = roll_number
        else:
            print("Invalid roll number!")

    # Private method
    def __display_details(self):
        print(f"Student Name: {self.name}, Roll Number: {self.__roll_number}")

    # Public method to access the private method
    def show_details(self):
        self.__display_details()  # Calling the private method internally

# Creating an object of the Student class
student = Student("Alice", 101)


print("<<<<<<<<< access public attributes and methods >>>>>>>>>>")
print("Name:", student.name)  # Public attribute
print("Roll Number:", student.get_roll_number())

print("<<<<<<<<< Modifying private attribute via setter >>>>>>>>>>")

student.set_roll_number(202)
print("Updated Roll Number:", student.get_roll_number())

student.set_roll_number("abc")

# Accessing private method indirectly
student.show_details()

print("<<<<<<<<< access private attributes and methods >>>>>>>>>>")
# print(student.__roll_number)  # AttributeError: 'Student' object has no attribute '__roll_number'.
# student.__display_details()   # AttributeError: 'Student' object has no attribute '__display_details'
