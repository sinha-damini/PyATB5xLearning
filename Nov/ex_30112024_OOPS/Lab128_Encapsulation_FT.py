# Web Automation - Selenium
# Page - You are going automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "daminisinha@gmail.com" and self.password == "Dami123":
            print("Allowed, Login Sucess")
        else:
            print("Login Failed")


# email = # Read from test data - Excel,CSV or Env file
# password = #Read from test data -Excel.CSV or Env file


Damini = VWOLoginPage("daminisinha@gmail.com", "Dami123")
Damini.login_confirm()

Pramod = VWOLoginPage("pramod@gmail.com", "Pramod123")
Pramod.login_confirm()