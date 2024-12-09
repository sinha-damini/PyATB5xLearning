class Parent:
    gold = "2kg"

    def __init__(self):
        print("DC - Parent")

    def BHK2(self):
        print("Parents has 2BHK")


class Child(Parent):

    def __init__(self):
        print("DC - Child")

    

    diamond = "Diamond"

    def BHK3(self):
        print("Child has 3BHK")

print("<<<<<<<<<<<<<Child inherits from Parent>>>>>>>>>>>>>>>>>>>>")
child_object= Child()
print(child_object.gold)
print(child_object.diamond)
child_object.BHK2()
child_object.BHK3()

print("<<<<<<<<<<<Parent can access only his attribute and methods.>>>>>>>>>>>")
father_obect_ref = Parent()

print(father_obect_ref.gold)
# print(father_obect_ref.diamond) #AttributeError: 'Parent' object has no attribute 'diamond'

father_obect_ref.BHK2()
# father_obect_ref.BHK3() #AttributeError: 'Parent' object has no attribute 'BHK3'.