# Sort a dictionary by its values in descending order
#my_dict = {"a": 3, "b": 1, "c": 2}
# {b: 1 , c: 2 , a :3}

my_dict = {"a": 3, "b": 1, "c": 2, "d": 3}
print(my_dict.items())
print(type(my_dict.items()))

# Sort a dictionary by its values in ascending  order
my_dict = {"a": 3, "b": 1, "c": 2}
#print(sorted(my_dict.items()))
sorted_dict=sorted(my_dict.items(),key=lambda item:item[1])
print(sorted_dict)
print(dict(sorted_dict))

#desending order
sorted_dict=sorted(my_dict.items(),key=lambda item:item[1],reverse=True)
print(sorted_dict)
print(dict(sorted_dict))
