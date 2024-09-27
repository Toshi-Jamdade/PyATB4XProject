class Dog:      # Class name always starts with Capital letter
    #A:
    name = None
    breed = None
    color = None
    #B
    def sleep(self):
        print("Sleeping")
    def bark(self):
        print("Barking")
    def eat(self, food):
        print(food)

dog1 = Dog()
print(dog1.name) #None
dog1.name = "Cherry"
print(dog1.name)       # Cherry

dog2 = Dog()
print(dog2.name) #None
dog2.name = "Tom"
print(dog2.name)    # Tom

dog3 = dog1
print(dog3.name)        # Cherry

