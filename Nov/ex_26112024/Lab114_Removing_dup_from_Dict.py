my_dict = {"a" : 10, "b" : 20, "c" : 50, "d" : 20, "e" : 30, "f" : 10}

uniue_values = set()
#A set unique_value is created.
# This set will be used to keep track of the values that have already been encountered
# while iterating over the dictionary.

result = {}
#An empty dictionary result is initialized.
# This will store the key-value pairs that have unique values.

for key,value in my_dict.items():
    if value not in uniue_values:
        result[key] = value
        uniue_values.add(value)

print(result)

# For key 'a' with value 10, it is added to result because 10 is not yet in unique_value.
# For key 'b' with value 20, it is added to result because 20 is not yet in unique_value.
# For key 'c' with value 50, it is added to result because 50 is not yet in unique_value.
# For key 'd' with value 20, it is skipped because 20 is already in unique_value.
# For key 'e' with value 30, it is added to result because 30 is not yet in unique_value.
# For key 'f' with value 10, it is skipped because 10 is already in unique_value.