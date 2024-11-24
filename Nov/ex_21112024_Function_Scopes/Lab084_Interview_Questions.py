#Check Leap Year
year = int(input("Enter year\n"))


def check_leap_year(year):
    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        return True
    else:
        return False

if check_leap_year(year):
    print("Yes", year, "is a leap year.")
else:
    print("No", year, "isn't a leap year.")



