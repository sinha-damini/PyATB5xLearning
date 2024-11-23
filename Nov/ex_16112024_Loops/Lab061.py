for i in range(5):
    if i == 3:
        print("abc")
        pass
        print(i)
# will do both the commands

print(" ______________________________ ")


for k in range(5):
    if k == 3:
        print("abc")
        pass
    print(k)
# will do both the commands


print(" ______________________________ ")


for j in range(5):
    if j == 3:
        continue
        print(j)
#it will not follow to prin(j) as current iteration would be skipped


print(" ______________________________ ")


for l in range(5):
    if l == 3:
        continue
    print(l)
# will print everything except for 3, as it is only asked to continue.
# Follow next one for clear understanding


print(" ______________________________ ")


for m in range(5):
    if m == 3:
        print("abc")
        continue
        print("ABC")
    print(m)
#will print abc, but not ABC as it will skip the current iteration from continue command.