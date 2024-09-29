#Inheritance
#Acquire the attributes & behaviour from another class

#Types of Inheritance
# Single - Used 85% of the times in API, Web Automation
# Multiple
# Multi Level
# Hybrid
# Hierarchical

# Single Inheritance:
class Father:
    key = "2BHK"

    def car(self):
        print("Father Car!", "ALTO")
        print("Father Car!", "ALTO", self.key)

class Son(Father):
    key2 = "3BHK"

    def home(self):
        print("3BHK")

    def bike(self):
        print("Bike")

father_obj = Father()
father_obj.car()
# Father Car! ALTO
# Father Car! ALTO 2BHK

son_obj = Son()
son_obj.car()
# Father Car! ALTO
# Father Car! ALTO 2BHK

son_obj.bike()  # Bike

print(son_obj.key)      # 2BHK