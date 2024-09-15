# Decorators in Python are a way to modify the behaviour of a function or class without changing its source code.

# They are powerful tool that allows you to wrap another function & extend its functionality, while keeping the original function's code unchanged.

def add_extra_security(func):
    #2 parts: wrapper & call
    def wrapper():
        print("Something is happening before a function is called.")
        print("Add helmet, gloves, knee guards")
        func()      #this is calling drive_bike
        print("Something is happening after a function is called.")
        print("Secure Driving")
    return wrapper()

@add_extra_security
def drive_bike():       #this will go to func beacuse @add_extra_security is added before it
    print("I am driving")

# Something is happening before a function is called.
# Add helmet, gloves, knee guards
# I am driving
# Something is happening after a function is called.
# Secure Driving


