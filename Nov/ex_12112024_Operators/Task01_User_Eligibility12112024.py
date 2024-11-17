# Task #1
#
# Write a program to take a user age and let him know if he can go the club.  21
#

age = int(input("Enter your age \n"))
# if(age>21):
#     print("You are eligible to go to the club.")
# else:
#     print("You aren't eligible to go to the club.")

print("You are eligible to go to the club." if(age>21) else "You aren't eligible to go to the club.")