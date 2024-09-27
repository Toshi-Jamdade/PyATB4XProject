# lambda expression:
# A lambda is an anonymous function that returns some form of data
import math


#Syntax:
# lambda parameters : expression
# parameters -> separated by commas
# expression -> An operation that return something

def triple_me(num):
    return num**3
output = triple_me(10)
print(output)               #1000

#The above code can be written in one line using lambda

o = lambda num : num**3
print(o(10))                    #1000

##############################################
def add_10(n):
    return n+10

result = lambda n : n+10
print(result(9))                    #19

################################################

def mul(a,b):
    return a*b

multiply = lambda a, b : a*b
print(multiply(10, 50))         #500

##############################################################

sum = lambda a,b,c : a+b+c
print(sum(10, 20, 35))      #65

########### Even Odd with lambda
find_even_odd = lambda num: "Even" if num%2==0 else "Odd"
print(find_even_odd(15))
print(find_even_odd(int(input("Enter the number: "))))
# Odd
# Enter the number: 100
# Even

########## Power of a number
op2 = lambda : math.pow(int(input("Enter the number: ")), 2)
print(op2())
# Enter the number: 9
# 81.0

