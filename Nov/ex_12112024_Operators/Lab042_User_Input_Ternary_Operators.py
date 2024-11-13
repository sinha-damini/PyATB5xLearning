#Program - if age > 18 - allowed to vote
#else - not allowed to vote


user_age = int(input("Enter your age \n"))
# if(user_age>18):
#     print("Yes, you can vote.")
# else:
#     print("No, you can't vote.")
print("Yes, you can vote." if user_age>18 else "No, you can't vote.")