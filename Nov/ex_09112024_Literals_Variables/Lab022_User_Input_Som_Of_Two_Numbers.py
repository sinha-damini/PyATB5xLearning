#Write a program to take 2 user input and then sum os those 2 numbers.
#mul -> *
#div -> /

#logic Building

"""

Step 1
I/P -> num1, num2 -> int
O/P -> sum - int, substraction - int, mul-int, div-float/int

Step 2
Rough Logic
sum,sub,mul,div,+,-,*,/
type of num1 and num2 is str
So, str --> int

Step 3
Real Logic
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("Sum is : ", sum)
print("Sub is : ", sub)
print("Mul is : ", mul)
print("Div is : ", div)

"""
num1 = int(input("Enter the number 1"))
num2 = int(input("Enter the number 2"))

# num1 = int(num1)
# num2 = int(num2)

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2


print("Sum is", sum)
print("Sub is", sub)
print("Mul is", mul)
print("Div is", div)

#num1 - 155
#num2 - 5