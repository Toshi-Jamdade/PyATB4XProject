#Write python program to calculate the area of a circle given its radius using the
# formula area=pi*r^2 (Take pi as 3.14)

# Logic building formula

# Step 1 Figure out the inputs & outputs
# input -> r -> data type -> float
# pi -> 3.14, math.pi
# power -> pow or ** -> any

# Output -> float - area, print area

# Step 2
# rough logic = area = 3.14 * pow(r,2)

# Step 3 - Write the logic
import math
radius = float(input("Enter the radius of the circle\n"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius,2)
area2 = 3.14 * (radius**2)
print("Area of the circle is", area)
print("Area of the circle is", area2)
print(f"Area of the circle is {area:2f}")

#Result:
# Enter the radius of the circle
#5
#5.0
#3.141592653589793
#Area of the circle is 78.53981633974483
#Area of the circle is 78.5
#Area of the circle is 78.539816

#In 1 Line:
print(3.14159*(float(input("Enter the radius\n"))**2))
#Result:
#Enter the radius
#4
#50.26544


