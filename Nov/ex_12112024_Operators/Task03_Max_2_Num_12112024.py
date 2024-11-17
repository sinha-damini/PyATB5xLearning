# Problem to find the max between two ( 3,4) → 4


num1 = float(input("Enter the first number:\n"))
num2 = float(input("Enter the second number:\n"))
# max_num = num1 if num1 > num2 else num2
# print("The max of given number is",max_num)

if num1 > num2:
    print("The max of given number is ", num1)
else:
    print("The max of given number is ",num2)