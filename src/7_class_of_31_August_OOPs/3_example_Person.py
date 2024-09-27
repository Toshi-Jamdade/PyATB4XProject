
class Person:
    #Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    weight = None
    gender = None
    phone_no = None

    #Behaviour:
    def talk(self):     #No Argument with No return
        #self will be the first argument in every behaviour
        print("I can talk")

    def sleep1(self, name):  #Argument with no return
        print("I am a method")
        print("Sleep", name)

    def sleep2(self, name):  #Argument with return
        print("I am a method")
        print("Sleep", name)
        return  None

    def walk(self):     #No Argument with No return
        print("I am walking")

    def walk_return(self):      #No Argument with return
        return  "I am walking"

# Create an object of the class Person:
# ObjectRef = ClassName()  --> Object

Toshi = Person()
Toshi.name = "Toshi Jamdade"
print(Toshi.name)       # Toshi Jamdade
Toshi.talk()        # I can talk

rajyalakshmi = Person()
rajyalakshmi.name = "Rajyalakshmi"
print(rajyalakshmi.name)        # Rajyalakshmi
rajyalakshmi.talk()      # I can talk





