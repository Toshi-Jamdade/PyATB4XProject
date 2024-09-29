# Multilevel Inheritance

class GrandFather:
    gold = "2 KG"

    def BHK1(self):
        print("1 BHK")

class Father(GrandFather):
    diamond = "22 carat"

    def bhk2(self):
        print("2 BHK")

class Son(Father):
    btc = "1 BTC"

    def bhk3(self):
        print("3 BHK")

s = Son()
print(s.btc)
print(s.gold)
print(s.diamond)
s.BHK1()
s.bhk2()
s.bhk3()

# 1 BTC
# 2 KG
# 22 carat
# 1 BHK
# 2 BHK
# 3 BHK