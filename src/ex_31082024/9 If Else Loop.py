# Conditions & Loops

# If Else Loop
#Syntax
# If Condition:
   # // code you want to execute if the condition is true
# else:
    #// // code you want to execute if the condition is false

#Write a program to take a user age and let him know if he can go to the club.
#21
#Logic Building
#1. user input - data type - int
# o/p -> String -> user if he can go or not

#2. Rough logic
#age > 21 -> print can go
#age < 21 -> print can't go

#3. write the logic
age=int(input("Enter your age\n"))
if age >= 21:
    print("Can go to the club")
else:
    print(f"Can't go to the club with this age -> {age}")

#Result:
#Enter your age
#24
#Can go to the club
#Enter your age
#15
#Can't go to the club with this age -> 15

