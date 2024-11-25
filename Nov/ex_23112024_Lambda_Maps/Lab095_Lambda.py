#Lambda without arguments.

import math
def pow_2(num):
    return math.pow(num,2)

op = pow_2(15)
print(op)

op2 = lambda : math.pow(int(input("Enter the num\n")), 2)
print(op2())
