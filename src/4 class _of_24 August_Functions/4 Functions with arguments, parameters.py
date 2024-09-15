# Functions with arguments, parameters:

def greet_by_name(name):
    print("Hello", name)

greet_by_name("Toshi")
greet_by_name(input("Enter your name: "))
greet_by_name(12345)
name = input("Enter your name: ")
greet_by_name(name)

# Hello Toshi
# Enter your name: tester
# Hello tester
# Hello 12345
# Enter your name: Monu
# Hello Monu