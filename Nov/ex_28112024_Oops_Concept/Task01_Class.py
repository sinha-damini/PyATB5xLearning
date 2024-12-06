# Create a Class PyATB , 5 Attributes, 3 Functions/Methods
# Use PC - to set the value of the attributes
# create a Print student information method/function
# 3 studetns objects
# PyATB().print_student_infomation()

class PyATB():
    # name = None
    # roll = None
    # gender = None
    # phone = None
    # address = None

    def __init__(self,name, roll, gender, phone, address):
        self.name = name
        self.roll = roll
        self.gender = gender
        self.phone = phone
        self.address = address

    def walk(self):
        print("They all can walk.")

    def talk(self):
        print("They all can talk.")

    def student_infomation(self):
        print(f"Name is {self.name}", f"Roll is {self.roll}", f"Gender is {self.gender}", f"Phone is {self.phone}",
              f"Address is {self.address}")

student1 = PyATB("Damini, ", 123, "Female, ", 12345, "Pune, ")
student2 = PyATB("Dhairya, ", 124, "Female, ", 45678, "Patna, ")
student3 = PyATB("Soumya, ", 456, "Male, ", 326496, "Kolkata, ")
student1.student_infomation()
student2.student_infomation()
student3.student_infomation()