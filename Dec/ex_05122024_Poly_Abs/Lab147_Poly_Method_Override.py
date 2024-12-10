class Parent:
    def home(self):
        print("2BHK")

    def town(self):
        print("10 BHK")


class Son(Parent):


    def home(self):
        print("3BHk")


ob_Ref = Son()
ob_Ref.home()
ob_Ref.town()