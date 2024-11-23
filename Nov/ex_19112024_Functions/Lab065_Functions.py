# def 123():
#     print('Hi 1')
# 123()

def _123():
    print('Hi 2')
_123()

def _():
    print('Hi 3')
_()

# def 123Abc():
#     print('Hi 4')
# 123Abc()

def Abc123():
    print('Hi 5')
Abc123()

def _123Abc():
    print('Hi 6')
_123Abc()

# Commanded functions will give error as identifier rules wasn't followed here.

print(" ---------------- ")
def h():
    print("Hello")
print("This is not a part of function because of intentation.")
h()
