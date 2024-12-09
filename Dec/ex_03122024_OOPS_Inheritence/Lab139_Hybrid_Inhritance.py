# Hybrid Inheritance

# multiple types of inheritance,
# such as single,
# multiple, and
# multilevel inheritance.

class A: # Father
    def methodA(self):
        return "Method A"

class B(A): # Pramod
    def methodB(self):
        return "Method B"

class C(A): # Lucky
    def methodC(self):
        return "Method C"


class D(B, C):  # Sister  # Multiple, Multilevel - MRO(Method Resolution Order - First
    def methodD(self):
        return "Method D"

a = A()
b = B()
c = C()
d = D()
print("<<<<<<<<<<< A has >>>>>>>>>>>>")
print(a.methodA())
print("<<<<<<<<<<< B has >>>>>>>>>>>>")
print(b.methodB())
print(b.methodA())
print("<<<<<<<<<<< C has >>>>>>>>>>>>")
print(c.methodC())
print(c.methodA())
print("<<<<<<<<<<< D has >>>>>>>>>>>>")
print(d.methodD())
print(d.methodB())
print(d.methodC())
print(d.methodA())
#'D' object has attribute 'methodA' as 'B' and 'C' inherited it from A.