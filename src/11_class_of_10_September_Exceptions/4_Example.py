# try, except, else and finally

try:
    num1 = int(input("Enter num1\n"))
    num2 = int(input("Enter num2\n"))
    result = num1/num2
except ValueError as ve:
    print("Value error, please enter integer")
except ZeroDivisionError as zde:
    print("Zero Div Error, don't use num2 as 0")
else:
    print(f"Result is {result}")
finally:
    print("This code will be always executed.")

