for i in range(0,101): # 0 to 100
    if i%2 == 0:
        print(i)

'''
should print 0,2,4,6,8,.....,100
'''

# | i | Condition | O/P
# | 0 | 0%2 = 0 -> True | O / P = 0
# | 1 | 1%2 = 0 -> False | O / P = Nothing will be printed
# | 2 | 2%2 = 0 -> True | O / P = 2
# | 3 | 3%2 = 0 -> False | O / P = Nothing will be printed
#.
#.
#.
#.
#.
# | 99 | 99%2 = 0 -> False | O / P = Nothing will be printed
# | 100 | 100%2 = 0 -> True | O / P = 100
