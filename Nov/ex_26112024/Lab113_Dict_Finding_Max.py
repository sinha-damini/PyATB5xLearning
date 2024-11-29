# function that returns the maximum value from a dictionary.
# {"a": 10, "b": 20, "c": 30}


def max_value_dict(dictionary):
    return max(dictionary.values())

print(max_value_dict({"a": 10, "b": 20, "c": 30}))

print("<<<<<<<<<<<<<2nd way, by taking user input>>>>>>>>>>>>>>>>")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Store the numbers in a dictionary
numbers = {"num1": num1, "num2": num2, "num3": num3}

# Find the maximum number by getting the maximum value from the dictionary
max_number = max(numbers.values())

# Print the result
print(f"The maximum number is: {max_number}")

print("<<<<<<<<<<<<<3rd way, by taking user input & using functions>>>>>>>>>>>>>>>>")

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

# Store the numbers in a dictionary
number = {"n1": n1, "n2": n2, "n3": num3}

# Find the maximum number by getting the maximum value from the dictionary
def max_value_dict(dictionary):
    return max(dictionary.values())

result = max_value_dict(number)
print("Max of given numbers are : ", result)

