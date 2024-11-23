#Write a program to finf sum of 3 numbers from user input.
#If user don't enter any number, use default 100, 200, 300.

num1=int(input("Enter num1\n"))
num2=int(input("Enter num2\n"))
num3=int(input("Enter num3\n"))

def sum_of_three_number(num1=100, num2=200, num3=300):
    return num1+num2+num3

result = sum_of_three_number(num1, num2,num3)
print("Sum is ",result)

result2 = sum_of_three_number()
print("Default Sum is ",result2)

result3 = sum_of_three_number(10, 20)
print("Default Sum is ",result3)