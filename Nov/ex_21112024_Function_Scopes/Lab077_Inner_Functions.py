def outer_function():
    var1 = 30
    var2 = 50

    def inner_function():
        var3 = 60
        print(var1)
        print(var2)
        print(var3)

    def inner_function2():
        print(var1)
        print(var2)
        # print(var3) -> var3 is local for inner_function()

    inner_function()
    inner_function2()

outer_function()