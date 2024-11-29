student_info1 = {
    "name" : "DAMINI",
            "age": 26,
"address": {
    "Current_Address": "Pune",
    "Permanent_Address": "Bihar"
}
}


student_info2 = {
    "name" : "VIVEK",
            "age": 30,
"address": {
    "Current_Address": "Kolkata",
    "Permanent_Address": "Bihar"
}
}


student_info3 = {
    "name": "Murthy",
    "age": 40,
    "address": {
    "Current_Address": "Chennai",
    "Permanent_Address": "Vizag"
    }
}

#Fetch permanent address of Murthy.
student_list = [student_info1,student_info2,student_info3]
print(student_list)
print(student_list[2])
print(student_list[2]["address"])
print(student_list[2]["address"]["Permanent_Address"])


#Alternate way
print(student_info3["address"]["Permanent_Address"])