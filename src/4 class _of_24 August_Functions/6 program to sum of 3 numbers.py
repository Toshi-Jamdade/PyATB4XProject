# Create a program to sum of 3 no.s from the user input.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

def sum_of_3_numbers(n1, n2, n3):
    return n1+n2+n3

result = sum_of_3_numbers(num1, num2, num3)
print(result)
result = sum_of_3_numbers(n1=num1, n2=num2, n3=num3)
print(result)
result = sum_of_3_numbers(10, 20, 30)
print(result)

# Enter num1: 190
# Enter num2: 700
# Enter num3: 500
# 1390
# 1390
#60
