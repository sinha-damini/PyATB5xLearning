class BaseTest:
    def open_browser(self):
        print("Starting the browser")

    def read_from_excel(self):
        print("Read from Excel")

    def close_browser(self):
        print("Close browser")


class TestCase1(BaseTest):

    def test_positive(self):
        self.open_browser()
        print("Test case P1 Executed!!")
        self.read_from_excel()
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Test case N1 Executed!!")
        self.close_browser()


class TestCase2(BaseTest):

    def test_2(self):
        self.open_browser()
        print("Test case P2 Executed!!")
        self.close_browser()


class TestCase3(BaseTest):

    def test_3(self):
        self.open_browser()
        print("Test case P3 Executed!!")
        self.close_browser()

print("************  The isinstance (obj, class) method  *************")

# used to check the relationship between the objects and classes.
# It returns true if the first parameter, i.e., obj is the instance of the second parameter, i.e., class.

class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
c = Calculation1()
print(isinstance(d,Calculation1))
print(isinstance(c,Calculation1))
print(isinstance(c,Derived))


print("************  The issubclass(sub,sup) method  *************")
# used to check the relationships between the specified classes.
# It returns true if the first class is the subclass of the second class, and false otherwise.
class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(issubclass(Derived,Calculation2))
print(issubclass(Calculation1,Calculation2))