# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is
# equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or
# scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

#Logic Building
# 1.
# i/p ->int/float -> s1,s2,s3
# O/p -> string
#
# 2. Rough Logic
# all sides are equal - s1=s2=s3
# exactly two sides are equal -> s1=s2 or s2=s3 0r s3=s1
# no sides are equal -> otherwise
#
# 3.
s1 = float(input("Length of 1st side \n"))
s2 = float(input("Length of 2nd side \n"))
s3 = float(input("Length of 3rd side \n"))
if(s1 == s2 == s3):
    print('The triangle is equilateral triangle.')
# elif(s1 == s2 or s2 == s3 or s3 == s1):
#     print('The triangle is isosceles triangle.')
# else:
#     print('The triangle is scalene triangle.')

elif(s1 != s2 and s2 != s3 and s3 != s1):
    print('The triangle is scalene triangle.')
else:
    print('The triangle is isosceles triangle.')


