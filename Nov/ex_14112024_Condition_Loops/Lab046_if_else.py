#Program to find maximum between 3 numbers.

#Logic building
# User Inputs -> num1,num2,num3 -> int
# o/p -> int or Str with max numbers
#
# Rough Logic
# num1>num2 and num1>num3 -> num1
# num2>num1 and num2>num3 -> num2
# else num3
#
# else-if condition
# Syntax:
# if(condition 1):
#     print('do 1')
# elif(condition 2):
#     print('do 2')
# elif(condition 3):
#     print('do 3')
# else(condition 4):
#     print('do for else')

num1 = int(input("Enter the number 1 \n"))
num2 = int(input("Enter the number 2 \n"))
num3 = int(input("Enter the number 3 \n"))
if(num1>num2 and num1>num3):
    print('Max of given  numbers is', num1)
elif(num2>num1 and num2>num3):
    print('Max of given  numbers is', num2)
else:
    print('Max of given  numbers is', num3)