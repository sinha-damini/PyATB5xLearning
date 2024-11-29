# Dictionary from Two Lists

keys = ["name", "role", "experience"]
keys1 = ["name", "role", "experience","last_name"]
values = ["Aman", "SDET", 3]
values1 = ["Aman", "SDET", 3, "Sinha"]

my_dict = dict(zip(keys, values))
my_dict2 = dict(zip(keys1, values1))
my_dict3 = dict(zip(keys, values1))
my_dict4 = dict(zip(keys1, values))
print(my_dict)
print(my_dict2)
print(my_dict3)#discarded extra value
print(my_dict4)#discarded extra key


# Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)
print(merged_dict.get("a"))
print(merged_dict["a"])