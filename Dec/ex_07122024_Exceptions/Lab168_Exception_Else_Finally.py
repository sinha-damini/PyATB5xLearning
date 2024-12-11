try:
    num1 = int(input("Enter a Number 1\n"))
    num2 = int(input("Enter a Number 2\n"))
    result = num1 / num2
except ValueError as e: #invalid literal for int() with base 10: 'hjjk'
    print(e)
except ZeroDivisionError as e: #division by zero
    print(e)
else:
    print("Output is ", result)