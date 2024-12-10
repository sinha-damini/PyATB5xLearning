# Single Inheritance
class Vehicle:
    def info(self):
        print("This is a vehicle.")

class Car(Vehicle):  # Single Inheritance
    def wheels(self):
        print("This car has 4 wheels.")

# Multilevel Inheritance
class ElectricCar(Car):  # Multilevel Inheritance
    def battery(self):
        print("This car is powered by a battery.")

# Hierarchical Inheritance
class Bike(Vehicle):  # Hierarchical Inheritance
    def wheels(self):
        print("This bike has 2 wheels.")

# Multiple Inheritance
class Boat:
    def float_on_water(self):
        print("This boat can float on water.")

class Amphibian(Vehicle, Boat):  # Multiple Inheritance
    def mode(self):
        print("This vehicle can move on both land and water.")

# Hybrid Inheritance
class Airplane(Vehicle, Boat):  # Combination of Multiple and Hierarchical
    def fly(self):
        print("This airplane can fly.")

# Single Inheritance
car = Car()
car.info()  # From Vehicle
car.wheels()  # From Car

# Multilevel Inheritance
electric_car = ElectricCar()
electric_car.info()  # From Vehicle
electric_car.wheels()  # From Car
electric_car.battery()  # From ElectricCar

# Hierarchical Inheritance
bike = Bike()
bike.info()  # From Vehicle
bike.wheels()  # From Bike

# Multiple Inheritance
amphibian = Amphibian()
amphibian.info()  # From Vehicle
amphibian.float_on_water()  # From Boat
amphibian.mode()  # From Amphibian

# Hybrid Inheritance
airplane = Airplane()
airplane.info()  # From Vehicle
airplane.float_on_water()  # From Boat
airplane.fly()  # From Airplane









# Single Inheritance
class Bank:
    def bank_info(self):
        print("Welcome to XYZ Bank!")

class Account(Bank):  # Single Inheritance
    def account_type(self):
        print("This is a savings account.")

# Multilevel Inheritance
class Customer(Account):  # Multilevel Inheritance
    def customer_details(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Customer Name: {self.name}, Balance: {self.balance}")

# Hierarchical Inheritance
class Loan(Bank):  # Hierarchical Inheritance
    def loan_info(self):
        print("This is a home loan.")

# Multiple Inheritance
class CreditCard:
    def credit_card_info(self):
        print("This is a Platinum Credit Card.")

class PremiumAccount(Customer, CreditCard):  # Multiple Inheritance
    def premium_features(self):
        print("Premium account with added benefits.")

# Hybrid Inheritance
class OnlineBanking(Account, CreditCard):  # Combination of Multiple and Hierarchical
    def online_services(self):
        print("Provides online banking services.")


# Single Inheritance
account = Account()
account.bank_info()  # From Bank
account.account_type()  # From Account

# Multilevel Inheritance
customer = Customer()
customer.bank_info()  # From Bank
customer.account_type()  # From Account
customer.customer_details("Alice", 15000)  # From Customer

# Hierarchical Inheritance
loan = Loan()
loan.bank_info()  # From Bank
loan.loan_info()  # From Loan

# Multiple Inheritance
premium = PremiumAccount()
premium.bank_info()  # From Bank
premium.account_type()  # From Account
premium.customer_details("Bob", 30000)  # From Customer
premium.credit_card_info()  # From CreditCard
premium.premium_features()  # From PremiumAccount

# Hybrid Inheritance
online = OnlineBanking()
online.bank_info()  # From Bank
online.account_type()  # From Account
online.credit_card_info()  # From CreditCard
online.online_services()  # From OnlineBanking
