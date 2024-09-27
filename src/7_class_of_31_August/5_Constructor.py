#Constructor
# Special function in the class, __init__()
# It will be automatically called when you create an object
# Two types:
    #a. Default with no argument
    #b. Parameterized - with argument
# Constructor doesn't return anything
# Name of the constructor is __init__
# Self means current object reference

# We can have multiple constructors, but try to avoid it as it creates confusion.

class Dog:
    name=None
    age=None

    def __init__(self, name, age):
        print("Called, object is created")
        self.name = name
        self.age = age

    def sleep(self):
        print("Sleeping")
        print("Who is sleeping ->" + self.name)
        print("Who is sleeping ->", self.name, self.age)

dog1 = Dog("Cherry", 5)    #Called, object is created
print(dog1.name)   #Cherry
print(dog1.age)     #5
dog1.sleep()
# Sleeping
# Who is sleeping ->Cherry 5

dog2 = Dog("Tom", 3)    #Called, object is created
print(dog2.name)    #Tom
print(dog2.age)     #3
dog2.sleep()
# Sleeping
# Who is sleeping ->Tom 3







