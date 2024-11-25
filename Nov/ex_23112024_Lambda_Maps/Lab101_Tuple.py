cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)
print("New Delhi" in cities)
#in is used to check if an element exists in a tuple.


t = (12, 34, 56)
# t.append(12) # AttributeError: 'tuple' object has no attribute 'append'
my_list = list(t)  #converted to list
print(my_list)
my_list.append(4) #appended to list.
t = tuple(my_list) #again converted to tuple
print(t)



ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
print(ENV_API_URLS)