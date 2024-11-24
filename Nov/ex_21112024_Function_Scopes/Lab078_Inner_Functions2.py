def outer_function():
    var1 = 30
    var2 = 50
    print(var1)
    print(var2)

def not_inner_function():
    var5 = 10
    print(var5)
    # print(var1)
    # print(var2)
    # var1 & var2 will not be accesible here.


not_inner_function()
outer_function()


print(" ------------------------------------------------------------------------ ")

def outer_function():
    var1 = 30
    var2 = 50
    print(var1)
    print(var2)

    def inner_function():
         var3 = 60
         var4= 80
         print(var1)
         print(var2)
         print(var3)

         def inner_function2():
             print(var1)
             print(var2)
             print(var3)
             print(var4)

         inner_function2()
    inner_function()
outer_function()
# inner_function()
# inner_function2()

#Try to understand from line27.
#in line 30 & 31 -> var1 & var2 is now global for inner_function()
#in line 35 to 38 -> var1, var2, var3 & var4 is now global for inner_function2()