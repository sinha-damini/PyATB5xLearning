for i in range(1,5):
    for j in range(1,3):
        print(i,j)



# 0
# 1 0
# 2 0 1
# 3 0 1 2
# 4 0 1 2 3

for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()

