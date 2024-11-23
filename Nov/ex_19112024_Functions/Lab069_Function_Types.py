#1. The can't return -> non return

#1. No Return Type and No Parameter / Argument -> NRNP

def greet():
    print("Hello")
greet()

print(" -------------------- ")
#2. No Return Type and with Argument -> NRWP
def greet_by_name(name):
    print("Hello,",name)
greet_by_name('Damini')

print(" -------------------- ")

#3. No Return Type with default Argument -> NRDP

def greet_default_arg(name="Damini"):
    print("Hello,",name)
    print("Hello,",name.upper())
greet_default_arg()
greet_default_arg('Vivek')

print(" -------------------- ")

def multiple_default_args(name1 = 'A', name2 = 'B'):
    print("Multiple Names->", name1, name2)
multiple_default_args()
multiple_default_args('Damini')
multiple_default_args(name1 = 'Damini')
multiple_default_args(name2 = 'Sinha')
multiple_default_args('Damini', 'Sinha')

print(" -------------------- ")

#4. Arguments with Return Type

def sum_of_two_num(a, b):
    return a+b

result = sum_of_two_num(5, 9)
print(result)

print(" -------------------- ")

#With Default Arguments

def sum_of_two_num_default(num1 = 100, num2 = 200):
    print("Sum of given numbers is: ")
    return num1+num2

result = sum_of_two_num_default(50, 60)
print(result)
result1 = sum_of_two_num_default(50)
print(result1)
result2 = sum_of_two_num_default(num2 = 50)
print(result2)
result3 = sum_of_two_num_default()
print(result3)


