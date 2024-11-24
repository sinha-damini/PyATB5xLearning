s1 = float(input("Length of 1st side \n"))
s2 = float(input("Length of 2nd side \n"))
s3 = float(input("Length of 3rd side \n"))


def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and b + c > a and a + c > b:
            if (a == b == c):
                return "Equilateral"
            elif (a == b or b == c or c == a):
                return "Isosceles"
            else:
                return "Scalene"
        else:
            print("Not a Triangle.")

    else:
        print("Not a valid length.")


result = classify_triangle(s1, s2, s3)
print("It is", result, "triangle.")
