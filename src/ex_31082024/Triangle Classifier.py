# Triangle Classifier

Side1 = float(input("Enter the length of Side1"))
Side2 = float(input("Enter the length of Side2"))
Side3 = float(input("Enter the length of Side3"))

if Side1==Side2==Side3:
    print("Equilateral Triangle")
#elif Side1 != Side2 != Side3:
    #print("Scalene Triangle")
elif Side1 == Side2 and Side1 != Side3:
    print("Isosceles Triangle")
elif Side1 == Side3 and Side1 != Side2:
    print("Isosceles Triangle")
elif Side2 == Side3 and Side2 != Side1:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
