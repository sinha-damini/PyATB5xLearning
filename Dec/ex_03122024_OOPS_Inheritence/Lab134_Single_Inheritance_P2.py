# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()


print("**************************************************************************************")


class Parent:


    def __init__(self,mother,father):
        self.mother = mother
        self.father = father
        print("DC - Parent")
        print("Mother is", mother)
        print("Father is", father)

    def BHK2(self):
        print("Parents has 2BHK")


class Child(Parent):

    def __init__(self,mother,father,child1,child2,child3):
        self.child1 = child1
        self.child2 = child2
        self.child3 = child3
        print("DC - Child")
        print("First child is", child1)
        print("Second child is", child2)
        print("Third child is", child3)

        # invoking the __init__ of the parent class
        Parent.__init__(self, mother,father)


    def BHK3(self):
        print("Child has 3BHK")


print("<<<<<<<<<<<<<Child inherits from Parent>>>>>>>>>>>>>>>>>>>>")

child_object = Parent("Sangita","Pranay")
child_object.BHK2()


print("<<<<<<<Child own methods>>>>>")

child_object = Child("Sangita","Pranay", "Dhairya", "Damini", "Soumya")
child_object.BHK3()


print("<<<<<<<<<<<Parent can access only his attribute and methods.>>>>>>>>>>>")
Mother_Father = Parent("Sangita","Pranay")
Mother_Father.BHK2()
# Mother_Father.BHK3() #'Parent' object has no attribute 'BHK3'.
