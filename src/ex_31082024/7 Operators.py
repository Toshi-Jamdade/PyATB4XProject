# Operators

# Assignment Operator -> = which is used to store the right value to the left value ref.
age = 24
print(age)      #24

# - -> unary operator
how_many_lambo_do_u_have = -1
print(how_many_lambo_do_u_have)         #-1

# Arithematic Operators
# +,-,*,/
print(2+2)
print(2-2)
print(2*2)
print(2/2)

# x//y  - Gives Quotient
# x%y   - Gives Remainder
# x**y  - Power
# ==    - Compare

print(3//2)     # 1 -> Quotient
print(7//5)     # 1 -> Quotient

print(7%5)      # 2 -> Remainder

print(2**2)     # 4 -> Power
print(2**3)     # 8 -> Power

print(2==2)     # True
print(2==3)     # False

# not operator --only works with boolean.
# In Python we use "not".
# "!" is used in JAVA.
is_pramod_married = True
print(not is_pramod_married)        #False

# Logical Operators -> Bool
# <, >, <=, >=
x=10
y=20
print(x>y)      #False
print(x<y)      #True

a=10
b=10
print(a>=b)     #True
print(a==b)     #True

# OR & AND
f=False
t=True
print(f or t)       #True
print(f and t)      #False

# "!" is used when we're using integer
# "not" is used when we're using boolean
x=10
y=20
result = (x != y)
print(result)           #True

#Ternary Operator
my_age = int(input("Enter your age"))
print("I will go to Goa" if my_age > 18 else "Can't go, stay home")

#if else
if my_age > 18:
    print("I will got to Goa")
else:
    print("Can't go, stay home")


