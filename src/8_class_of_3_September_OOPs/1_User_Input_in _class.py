#Take user input & create a class

class Person:
    def __init__(self):
        self.name = input("Enter your name\n")
        self.age = input("Enter your age\n")
        self.phone = input("Enter your phone no\n")
        self.occupation = input("Enter your occupation\n")

    def display_information(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone no is {self.phone}")
        print(f"Occupation is {self.occupation}")

#Create an object
person1 = Person()

#call the display function
person1.display_information()

# Enter your name
# Toshi
# Enter your age
# 24
# Enter your phone no
# 987654
# Enter your occupation
# Job
# Name is Toshi
# Age is 24
# Phone no is 987654
# Occupation is Job