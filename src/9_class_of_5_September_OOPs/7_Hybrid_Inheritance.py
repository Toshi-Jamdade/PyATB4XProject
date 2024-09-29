# Hybrid Inheritance

class A:
    def methodA(self):
        return "Method A"

class B(A):
    def methodB(self):
        return "Method B"

class C(A):
    def methodC(self):
        return "Method C"

class D(B, C):
    def methodD(self):
        return "Method D"

a=A()
b=B()
c=C()
d=D()

print(b.methodA())
print(d.methodA())
print(d.methodB())
print(d.methodC())

# Method A
# Method A
# Method B
# Method C