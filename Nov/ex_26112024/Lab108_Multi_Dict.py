student_info1 = {
    "name" : "DAMINI",
            "age": 26,
"address": {
    "Current_Address": "Pune",
    "Permanent_Address": "Bihar"
}
}
print(student_info1)


student_info2 = {
    "name" : "VIVEK",
            "age": 30,
"address": {
    "Current_Address": "Kolkata",
    "Permanent_Address": "Bihar"
}
}
print(student_info2)

student_list = [student_info1, student_info2]
print(student_list)
print(student_list[1])
print(student_list[1]["address"])
print(student_list[1]["address"]["Current_Address"])
