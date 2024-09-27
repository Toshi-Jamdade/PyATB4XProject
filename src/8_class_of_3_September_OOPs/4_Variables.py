#Class variable
#Method
    #Public - variable - Don't mention anything
    #Protected - _
    #Private - __
# Inheritance
# Polymorphism
# Abstraction
# Encapsulation
# Static Method

# Variables
    #Local variable (within functions/block of code)
    #Global variable
    #Instance variable (within the class)
    #Static variable

a=10    #global variable

class Person:
    b=11    #instance variable

    def print_info(self):
        print(a)
        print(c)
        print(self.b)
        global d    #Declare it as global
        d = "Hello"
        print(d)

c=20    #global variable

obj_ref = Person()
obj_ref.print_info()
print(a)
print(d)
#print(b)        #NameError: name 'b' is not defined

# 10
# 20
# 11
# Hello
# 10
# Hello
