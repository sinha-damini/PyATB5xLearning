# ✅ FizzBuzz Test:
#
# Write a program that prints numbers from 1 to 100.
# However, for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."
# ( for, if)

for i in range(1, 101):  # 1 to 100
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz", i)
        # print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz", i)
        # print("Fizz")
    elif i % 5 == 0:
        print("Buzz", i)
        # print("Buzz")
    else:
        print(i)

'''
Tried with below code also

for i in range(1, 101):# 1 to 100
    
    if i%3 == 0:
        print("Fizz", i)
    elif i%5 == 0:
        print("Buzz", i)
    elif (i%3 == 0) and (i%5 == 0):
        print("FizzBuzz", i)

It wasn't going to code 
elif (i%3 == 0) and (i%5 == 0):
        print("FizzBuzz", i)
'''
