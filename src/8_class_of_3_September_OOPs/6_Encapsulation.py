#Encapsulation
# bind the data variables with the methods
# Data member - class variables
#Hide the data members (class variables, instance variables)
# by using only the methods

class Car:
    model=None
    name = None
    password = 123

    def __init__(self):
        print("DC")

    def change_password(self):
        self.password="toshi"

    def change_password2(self):
        print(self.password)

obj_ref = Car()
#print(obj_ref.password)     #'Car' object has no attribute 'password'

#obj_ref.change_password2()