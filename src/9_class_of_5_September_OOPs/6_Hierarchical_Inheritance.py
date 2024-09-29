# Hierarchical Inheritance

class Father:
    def home(self):
        print("4 BHK")

class Son(Father):
    pass

class Daughter(Father):
    pass

class Son2(Father):
    pass

s=Son()
d=Daughter()
s2=Son2()

s.home()
d.home()
s2.home()

# 4 BHK
# 4 BHK
# 4 BHK
