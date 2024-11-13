# #Write a python program to calculate the
# area of circle given its radius, using the formula
# area = pi*r^2, take pi = 3.14

r = float(input("Enter the radius \n"))
# area = 3.14*pow(r,2)
area = 3.14*(r ** 2)
print("Area of circle is ",area)
print(f"Area of circle is {area:.3f}")
'''

Enter the radius 
258
Area of circle is  209010.96000000002
Area of circle is 209010.960

'''
########## 2nd Way ###########
'''
import math
r = float(input("Enter the radius \n"))
area = math.pi*math.pow(r,2)
print("Area of circle is ",area)


Enter the radius 
258
Area of circle is  209116.973393551

'''