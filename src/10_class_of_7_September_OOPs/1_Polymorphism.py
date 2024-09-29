# Polymorphism

# Objects -> can have many forms
    # Behaviours -> can be different based on who is calling

# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# Method overriding, Method Loading

# Method overriding - Child or subclass can have the same name method as the parent or superclass.

class Shape:
    a=10

    def area(self):
        print("Area of the shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    b=5
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        super().area()      # calling Parent class behaviour by using super()
        print(super().a)    # calling Parent class attribute by using super()
        print(self.b)       # calling own class attribute by using self
        return 3.14 * self.radius * self.radius

shape1 = Rectangle(3, 4)
print(shape1.area())        # 12

shape2 = Circle(10)
print(shape2.area())
# Area of the shape
# 10
# 314.0


