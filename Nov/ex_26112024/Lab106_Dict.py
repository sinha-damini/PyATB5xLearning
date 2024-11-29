my_dict = {
    "name" : "Damini",
    "age"  : 26,
    "role" : "SDET",
    "experience" : 3
}

print(my_dict)

#Another way

my_dict_2 = dict(name="Damini", age = 26, address ="Pune")
print(my_dict_2)

#Accessing  values.
t = my_dict["age"]
print(t)
print(my_dict_2["age"])

# - `Adding/Updating a Key-Value Pair: my_dict[key] = value
my_dict["experience"] = 3.5 #updated
my_dict_2["State"] = "Maharashtra" #added

print(my_dict)
print(my_dict_2)

#Removing a key : del my_dict[key]

del my_dict_2["address"]
print(my_dict_2)

#iterating over a dictionary.

for key, value in my_dict.items():
    print(key, " -> ", value)

print("<<<<<<<<<<< Only values>>>>>>>>>>>")
for key, value in my_dict.items():
    print(value)
print("<<<<<<<<<<< Only keys>>>>>>>>>>>")

for key, value in my_dict.items():
    print(key)


#We can print True or False.
print("<<<<<<<<<<<     >>>>>>>>>>>")
print("address" in my_dict_2)
print("role" in my_dict)
