for i in range(1,5):
    for j in range(1,3):
        print(i,j)

print(" &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ")
#i
# 0
# 1 1
# 2 2 2
# 3 3 3 3
# 4 4 4 4 4

#j
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
n = int(input("Enter no. of rows\n"))

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

# i = 0, 1, 2, 3, 4
# when i= 0
# j (1)
# j = 0
# when i= 1
# j (2)
# j = 0, 1
# when i= 2
# j (3)
# j = 0, 1, 2
# when i= 3
# j (4)
# j = 0, 1, 2, 3
# when i= 4
# j (5)
# j = 0, 1, 2, 3, 4

print(" &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ")

for i in range(n):
    for j in range(i+1):
        print(i, end=" ")
    print()