my_list = [1, 2, 3]

# Indexing
print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

# append() - # Append object to the end of the list.
my_list.append(4)
my_list.append(5)
my_list.append("Damini")
print(my_list)

# extend() - Append a new list to the end of the list.
my_list.extend([7, 8, 10, 9])
print(my_list)
print(len(my_list))

# insert() - Insert an element a specific index.
my_list.insert(1, "Dutta")
print(my_list)
print(len(my_list))#length increased as we have inserted not replaced the element

my_list.insert(0, 0)
print(my_list)
print(len(my_list))#length increased as we have inserted not replaced the element

my_list[1] = "Amit"
print(my_list)
print(len(my_list))#length not increased as we have replaced the element at specific index

# remove()
my_list.remove("Amit")
print(my_list)

print(" --------------------------")
print(" --------------------------")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)
#We can copy the list.

my_copy_list.remove("Dutta")
my_copy_list.remove("Damini")
my_list.remove("Dutta")
my_list.remove("Damini")

my_copy_list.sort()
#Sort the elements. But elements should be of same data type.

print(my_list)
print(my_copy_list)

a=["Adfh","Sfgiu;","Gddfj",'btfio',"Bgfdfku"]
a.sort()
print(a)