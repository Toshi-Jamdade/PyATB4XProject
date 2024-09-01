# if - elif - else Loop:

#Find max bet 3 no.s
#Logic building
#1. user input -> num1, num2, num3 -> integers
# o/p -> int or str with max number

#2. Logic

# if - elif - else Loop:
#Syntax
#if condition 1:
#   print("do 1")
#elif condition 2:
#   print("do 2")
#else:
 #   print("do 3")

num1 = int(input("Enter the num1\n"))   #5
num2 = int(input("Enter the num2\n"))   #3
num3 = int(input("Enter the num3\n"))   #2

# 5>3 and 5>2 -> true -> 5
# num1>num2 and num1>num3 -> num1

# 3>5 and 3>2 ->
# num2>num1 and num2>num3 -> num2

if num1>num2 and num1>num3:
    print(f"Num1 is greater -> {num1}")
elif num2>num1 and num2>num3:
    print(f"Num2 is greater -> {num2}")
else:
    print(f"Num3 is greater -> {num3}")

# Instead of if else, we can also use below
result = max(num1, num2, num3)
print(result)