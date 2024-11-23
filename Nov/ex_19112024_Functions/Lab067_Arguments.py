#function without arguments.

def say_hello():
    print("Hello!")
say_hello()

print(" -------------------------- ")

#function with arguments and parameters.
def say_hello_by_name(name):
    # print("Hello!, ",name)
    print(f"Hello!, {name}")
say_hello_by_name("Damini")
say_hello_by_name(123)
say_hello_by_name(3.14)
