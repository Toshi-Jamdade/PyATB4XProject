# Method Overloading
# Python does not support method overloading in the traditional sense.

class MathUtils(object):    # is a object - single inheritance

# Method overloading - not supported!

    def add(self, a, b):
        return a+b

    def add(self, a, b, c):
        return a+b+c

math = MathUtils()
op2 = math.add(1, 2, 3)
print(op2)      #6
# op1 = math.add(1, 2)    #TypeError: MathUtils.add() missing 1 required positional argument: 'c'


#If we give default value of c then only i=method overloading is supported:

class MathUtils(object):
    def add(self, a, b):
        return a+b
    def add(self, a, b, c=0):   #Default value is given as 0
        return a+b+c
math = MathUtils()
op1 = math.add(1, 2)
print(op1)      #3

