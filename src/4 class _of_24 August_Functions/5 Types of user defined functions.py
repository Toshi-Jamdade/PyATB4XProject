# Types of User Defined Functions:
# 1. They can't return anything.
# 2. They can return something.
# They have parameters.
# They don't have parameters.

# 1. They can't return anything. -> no return:

    # A) No return type & no parameter/Argument - NRNP
def greet():
    print("Hello world")
result = greet()
print(result)
# Hello world
# None

    # B) No return type with argument.
def greet_by_name(name):
    print("Hello", name)
greet_by_name("Toshi")
# Hello Toshi

    # C) No return type with default argument.
def say_hello_default_arg(name="Toshi"):
    print("Hello", name)
say_hello_default_arg("Abcd")
say_hello_default_arg()
say_hello_default_arg(name="TestName")      #this is called as positional argument
# Hello Abcd
# Hello Toshi
# Hello TestName

    # D) multiple arguments:
def multiple_args(name1="Inky", name2="Pinky", name3="Ponky"):
    print("Multiple arguments", name1, name2, name3)
multiple_args(name1="Ram", name2="Amit", name3="Deepika")
multiple_args()
# Multiple arguments Ram Amit Deepika
# Multiple arguments Inky Pinky Ponky

#2. They can return something.

    # E) Argument + return type:
def sum_of_two_numbers(num1=40, num2=60):
    return num1+num2
result = sum_of_two_numbers(10, 200)
print(result)
result = sum_of_two_numbers()
print(result)
#210
#100