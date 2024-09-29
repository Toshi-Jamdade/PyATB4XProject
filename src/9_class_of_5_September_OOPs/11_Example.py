class GF:
    def car(self):
        return "Old car"

class F(GF):
    def car(self):
        return "Honda"

class S(F):
    def car(self):
        return "Lambo"

son = S()
GrandFather = GF()

print(GrandFather.car())
print(son.car())

# Old car
# Lambo
