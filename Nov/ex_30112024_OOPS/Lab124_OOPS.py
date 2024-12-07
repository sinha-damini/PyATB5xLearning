a= 10

class Person:
    b = 20 #Instance Variable -> Belong to class

    def print_info(self):
        c = 30 # Local Variable
        # print(self.c) -> 'Person' object has no attribute 'c'
        print(c) #-> For local varible we don't need to use self'
        print(self.b)
        global a
        print(a)

objec_ref = Person()
objec_ref.print_info()


"""

**Local variables **
Can be access directly.
Local variable always have a high preference** as compared with global variable
**Instance variable**
Can be accessed by the self keyword. 


"""