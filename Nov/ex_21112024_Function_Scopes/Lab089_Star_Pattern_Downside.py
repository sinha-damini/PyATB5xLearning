
for i in range(6,0,-1):
    for j in range(i-1):
        print(j, end=" ")
    print()

for i in range(4,-1,-1):
    for j in range(i+1):
        print(j, end=" ")
    print()


for i in range(5,0,-1):
    for j in range(i):
        print(i, end=" ")
    print()

print(" &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ")

n = int(input("Enter no. of rows\n"))
for i in range(n-1,-1,-1):
    for j in range(i+1):
        print("*", end=" ")
    print()

print(" &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ")

n = int(input("Enter no. of rows\n"))
for i in range(n+1,0,-1):
    for j in range(i-1):
        print("*", end=" ")
    print()

print(" &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ")

n = int(input("Enter no. of rows\n"))
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0


print(" <<<<<<<<<<<<<<<&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&>>>>>>>>>>>>>>> ")

n = int(input("Enter no. of rows\n"))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()