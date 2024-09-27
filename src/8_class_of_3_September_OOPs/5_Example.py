#Web automation - Selenium
#Page - You are going to automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "toshi@gmail.com" and self.password == "Pass@123":
            print("Allowed to login")
        else:
            print("Not allowed")

email=input("Enter the email\n")
password = input("Enter the password\n")

vwo_obj=VWOLoginPage(email, password)
vwo_obj.login_confirm()

# Enter the email
# toshi@gmail.com
# Enter the password
# Pass@123
# Allowed to login

# Enter the email
# toshi@gmail.com
# Enter the password
# 123
# Not allowed

