import math
# math.exp(1000) #OverflowError: math range error

try:
    math.exp(1000) # math range error
except Exception as e:
    print(e)