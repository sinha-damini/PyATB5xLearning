def decorator_1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper


def decorator_2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator_2
@decorator_1
def say_hello():
    print("Hello!")


say_hello()

