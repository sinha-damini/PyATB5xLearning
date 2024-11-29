dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2}


print(set(dict1.values()))
##<class 'set'>



print(dict1.values())
print(type(dict1.values()))
#<class 'dict_values'>

print(dict1.keys())
print(type(dict1.keys()))
#<class 'dict_keys'>

print(set(dict1.keys()))
print(type(set(dict1.keys())))
#<class 'set'>

missing_keys = set(dict1.keys()) - set(dict2.keys())
missing_keys_1 = dict1.keys() - dict2.keys()

print(missing_keys)
print(missing_keys_1)
print(type(missing_keys))
#<class 'set'>
print(type(missing_keys_1))
# <class 'set'> ->>>>>>>>> It's not #<class 'dict_keys'>.

# Sort a dictionary by its values in ascending order
#will do this later
my_dict = {"a": 3, "b": 1, "c": 2}

# {b: 1 , c: 2 , a :3}