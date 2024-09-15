# Functions Scope

global_b = 12
def my_function():
    a=10    #local variable within the function
    print(a)
    print(global_b)

def f():
    global_b=15
    print(global_b)

#print(a)   - this will give error because a is a local variable and cannot be called outside of the function
my_function()
f()
print(global_b)

# 10
# 12
# 15
# 12