#Task for Today
#Take 2 i/p from the user
#print the quotient and remainder.
#num1 - 15
#num2 - 2
#Q - 7
#R - 1

num1 = float(input("Enter the number 1 "))
num2 = float(input("Enter the number 2 "))

print("Quotient of given number =", num1//num2)
print("Remainder of given number =", num1%num2)



#2nd way
Quotient, Remainder = divmod(num1,num2)
print("Quotient of given number =", Quotient)
print("Remainder of given number =", Remainder)
'''
// -> floor division
% -> modulus operator
'''

"""
Enter the number 1 15
Enter the number 2 2
Quotient of given number = 7.0
Remainder of given number = 1.0
Quotient of given number = 7.0
Remainder of given number = 1.0




Enter the number 1 1326497976569
Enter the number 2 26496
Quotient of given number = 50064084.0
Remainder of given number = 6905.0
Quotient of given number = 50064084.0
Remainder of given number = 6905.0

"""