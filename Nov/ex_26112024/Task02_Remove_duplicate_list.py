# my_list = [1, 2, 2, 3, 4, 4, 5]
# Remove duplicates from a list using a set.
# Output: [1, 2, 3, 4, 5]

my_list = [1, 2, 2, 3, 4, 4, 5]
my_list_2 = set(my_list)
# print(my_list_2)

result = list(my_list_2)
print(result)


print("<<<<<<<<<< 2nd way >>>>>>>>>>>>>>>>>")
print(list(set(my_list)))