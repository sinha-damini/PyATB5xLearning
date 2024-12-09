# Method Overloading


class MathUtils:
    # Method - overloading - Not
    # supported!
    def add(self, a=10, b=20):
        return a + b

    def add(self, a=1, b=1, c=1):
        return a + b + c

    def add(self, a=1, b=0, c=0, d=0):
        return a + b + c + d


math = MathUtils()
op1 = print(math.add(1, 2))
op2 = print(math.add())
op3 = print(math.add(10,20,30,40))
