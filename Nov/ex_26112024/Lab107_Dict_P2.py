student_info = {
    "name": "Damini",
    "age": 26,
    "address": "Pune"
}

print(student_info["name"])
print(student_info["age"])
print(student_info["address"])

student_info["age"] = 50
print(student_info)

student_info2 = dict(name="Damini Sinha", age=26, address="Pune")
print(student_info2)


#Dictionary withinn dictionary.
student_info1 = {
    "name" : "DAMINI",
            "age": 26,
"address": {
    "Current_Address": "Pune",
    "Permanent_Address": "Bihar"
}
}
print(student_info1)
