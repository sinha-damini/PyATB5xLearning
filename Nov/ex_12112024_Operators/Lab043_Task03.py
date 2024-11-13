# Problem to find the max between two ( 3,4) → 4


num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
max_num = num1 if num1 > num2 else num2
print("The max of given number is",max_num)