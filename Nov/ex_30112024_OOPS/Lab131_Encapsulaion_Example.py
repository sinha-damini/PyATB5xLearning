
class Bank:
    def __init__(self,account_number, balance):
        self.balance = balance # public instance variable
        self.__account_number = account_number # private instance variable
        print(self.__account_number)
        print(self.balance)

    def check_balance(self):
        print("<<<<<<<<<<<<<<<<< check_balance() >>>>>>>>>>>>>>>>>>>")
        print(self.__account_number)
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("<<<<<<<<<<<<<<<<< deposit() >>>>>>>>>>>>>>>>>>>")
        print(self.__account_number)
        print(self.balance)

axis = Bank(123456789, 400)
axis.deposit(5000)
axis.check_balance()
print("<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>")
print(axis.balance)
# print(axis.__account_number) -> 'Bank' object has no attribute '__account_number'.