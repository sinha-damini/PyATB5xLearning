# Method Overloading is Not Supported - Python
class Calc:

    # def sum(self, a, b):
    #     return a + b
    # It will give result 8

    def sum(self, a, b, c=1):
        return a + b + c

    def sum(self, a, b):
        return a + b


calc_ref = Calc()
result = calc_ref.sum(3, 4)
print(result)