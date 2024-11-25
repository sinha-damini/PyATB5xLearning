#Lambda

'''
def add(n):
    return num + 10 #num = num + 10

result = add(2)
print(result)

def mul(a,b):
    return a*b

result = mul(5, 3)
print(result)
'''

result =  lambda num :  num + 10
print(result(2))

result_m = lambda a,b : a*b
print(result_m(5, 3))