# Exceptions
# Any event which disrupts the normal flow of a program when an error occurs.

# Exceptions:
# ArithmeticError
#     ZeroDivisionError
#     FloatingPointError
# NameError
# ExceptionGroup
# ValueError
# TypeError
# OSError
#     PermissionError
#     FileNotFoundError
# RuntimeError

# Errors and exceptions in Python are both mechanisms that indicate problems in a program.

# Error
# These are typically caused by mistakes in the code, such as syntax errors or logical flaws.
# Errors are something which are difficult to recover.
# Errors are more severe issues
# For e.g: a Syntax error

# Exceptions
# These are run time issues that occur during the execution of a program.
# Exceptions can be handled.
# e.g: trying to divide by zero or accessing an invalid index in a list.
# e.g: a TypeError occurs when an operation is performed on incompatible data types.

# print(x)        # NameError: name 'x' is not defined

# print(10/0)     # ZeroDivisionError: division by zero

# print(1+"1")        # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print(int('a'))     # ValueError: invalid literal for int() with base 10: 'a'

# my_list = [1,2,3]
# print(my_list[5])       # IndexError: list index out of range

# while True print(I "Hello World")   # SyntaxError: invalid syntax

    # print(I "Hello World")      # IndentationError: unexpected indent