import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total time taken by the funcion =", end_time-start_time)
    return wrapper()





@time_decorator

def test_ui_1():
    print("add a function, time taken by this function 1.")
    time.sleep(2)

print("______________________________")

@time_decorator

def test_ui_2():
    print("add a function, time taken by this function 2.")
    time.sleep(5)


"""

1732460833.5523758 -> print(start_time)
add a function, time taken by this function 1. -> print("add a function, time taken by this function 1.")
1732460835.553042 -> print(end_time)
Total time taken by the funcion = 2.0006661415100098 -> print("Total time taken by the funcion =", end_time-start_time)
______________________________
1732460835.5530984
add a function, time taken by this function 2.
1732460840.5538087
Total time taken by the funcion = 5.0007102489471436

"""