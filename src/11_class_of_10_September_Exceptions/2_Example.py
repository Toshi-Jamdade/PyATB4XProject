# try
# except
# else:
# finally:

# try:
    # Try this code, if error
# except:
    # Execute me if try has some error

print("Start of the program")
try:
    a = int(input("Enter num1\n"))
    b = int(input("Enter num2\n"))
    c = a/b
    print("Result Div is ", c)
except Exception as e:      # Exception is a class that contains all types of exceptions that we have
    print(e)
    print("Please check your inputs, it should not be a string or zero")
print("End of the program")

# Start of the program
# Enter num1
# 10
# Enter num2
# t
# invalid literal for int() with base 10: 't'
# Please check your inputs, it should not be a string or zero
# End of the program

# Start of the program
# Enter num1
# 80
# Enter num2
# 0
# division by zero
# Please check your inputs, it should not be a string or zero
# End of the program

###################################################################
# Without exception handling following error will come:

# Enter num1
# 9
# Enter num2
# 0
# ZeroDivisionError: division by zero

# Enter num1
# 90
# Enter num2
# abc
# ValueError: invalid literal for int() with base 10: 'abc'

###################################################################

