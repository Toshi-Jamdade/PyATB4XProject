class Calculator:
    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return  a+b
    def sub(self, a, b):
        return  a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a/b

object_ref = Calculator()

output_sub = object_ref.sub(3, 4)
output_mul = object_ref.mul(5, 6)
output_sum = object_ref.sum(8, 9)
output_div = object_ref.div(3, 4)

print(output_div,output_sum, output_mul, output_sub)

a=int(input("Enter the value of a\n"))
b=int(input("Enter the value of b\n"))
output_sub = object_ref.sub(a, b)
output_mul = object_ref.mul(a, b)
output_sum = object_ref.sum(a, b)
output_div = object_ref.div(a, b)

print(output_div,output_sum, output_mul, output_sub)

# DC
# 0.75 17 30 -1
# Enter the value of a
# 70
# Enter the value of b
# 10
# 7.0 80 700 60