# Multiple Inheritance

class Father:
    def father_money(self):
        return 5
    def home(self):
        return "This is from the father"

class Mother:
    def mother_money(self):
        return 2

    def home(self):
        return "This is from the mother"

class Son(Mother, Father):
    pass

class Son2(Father, Mother):
    pass

s=Son()
print(s.mother_money())     # 2
print(s.father_money())     # 5
print(s.home())         # This is from the mother --
# Since, Mother is the first class inherited by Son, hence home() is called from Mother class. #MRO - Method resolution order

print()

s2 = Son2()
print(s2.home())        #This is from the father
# Since, Father is the first class inherited by Son, hence home() is called from Father class.



