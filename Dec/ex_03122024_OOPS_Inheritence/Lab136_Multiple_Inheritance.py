#Not supported in Java.


class Father:

    def home(self):
        return "This is from the Father"
    def father_money(self):
        return 5


class Mother:

    def home(self):
        return "This is from the Mother just as Father."
    def home2(self):
        return "This is from the Mother"
    def mother_money(self):
        return 2


# class Son(Mother, Father): # Multiple In - FCFS

class Son(Mother, Father):

    def print_info(self):
        print("Son")



s = Son()
s.print_info()
print(s.father_money())
print(s.mother_money())
print(s.home()) #Both has same method name.  It will return whichever will be First Inherited
print(s.home2())