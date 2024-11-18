for number in range(10): # 0 to 9 : 10 times
    if number%2 == 0:
        continue
    else:
        print(number)


# | i | Condition | O/P
# | 0 | 0%2 = 0 -> True | O / P = continue -> skip and go back
# | 1 | 1%2 = 0 -> False | O / P = 1
# | 2 | 2%2 = 0 -> True | O / P = continue -> skip and go back
# | 3 | 3%2 = 0 -> False | O / P = 3
#.
#.
#.
# | 9 | 9%2 = 0 -> False | O / P = 9