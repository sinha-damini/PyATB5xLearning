# Multilevel Inheritance
# GF -> F -> Son


class GrandFather:
    gold = "2kg"

    def bhk1(self):
        print("1BHK")


class Father(GrandFather):
    diamond = "22 karat"

    def bhk2(self):
        print("2BHK")


class Son(Father):
    btc = "1BTC"

    def bhk3(self):
        print("3BHK")


s = Son()
f = Father()
g = GrandFather()

print("<<<<<<<<<<< Son inherits from both father and grand father >>>>>>>>>>>>")
print(s.gold)
print(s.diamond)
print(s.btc)
s.bhk1()
s.bhk2()
s.bhk3()

print("<<<<<<<<<<< Father inherits from grand father >>>>>>>>>>>>")
print(f.gold)
print(f.diamond)
# print(f.btc)
# 'Father' object has no attribute 'btc'
f.bhk1()
f.bhk2()
# f.bhk3()
#'Father' object has no attribute 'bhk3'

print("<<<<<<<<<<< Grand father has its own only. >>>>>>>>>>>>")
print(g.gold)
# print(g.diamond)
# print(g.btc)
# 'GrandFather' object has no attribute 'diamond' and 'btc'
g.bhk1()
# g.bhk2()
# g.bhk3()
#'GrandFather' object has no attribute 'bhk2' and 'bhk3'.
