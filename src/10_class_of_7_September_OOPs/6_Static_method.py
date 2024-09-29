# Static methods
# A method that belongs to a class rather than an instance of the class.

class MathOp:

    def div(self, a, b):
        return a/b

    @staticmethod
    def sum(a, b):
        return a+b

o=MathOp()
output=o.div(10, 5)
print(output)       # 2.0

# Static methods can be called directly without the object.
print(MathOp.sum(3,5))      # 8