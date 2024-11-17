# Checking for a Leap Year , 2024 → Yes

# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.

#Logic Building
# 1.
# i/p ->int
# O/p -> string
#
# 2. Rough Logic
# Number divisible by 400
# and num div by 4 but not by 100
# divisible means remainder should be 0
#
# 3.
year = int(input("Enter year \n"))
if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")