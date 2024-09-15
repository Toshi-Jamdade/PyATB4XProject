# Decorators in Python are a way to modify the behaviour of a function or class without changing its source code.

# They are powerful tool that allows you to wrap another function & extend its functionality, while keeping the original function's code unchanged.

def my_decorator(func):
    #2 parts: wrapper & call
    def wrapper():
        print("Something is happening before a function is called.")
        func()
        print("Something is happening after a function is called.")
    return wrapper()

def drive_bike():
    print("I am driving")

drive_bike()