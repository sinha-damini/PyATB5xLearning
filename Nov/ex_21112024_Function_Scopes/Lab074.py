pb_global_b = 12

def my_function():
    pb_local_a = 10
    print(pb_local_a)
    print(pb_global_b)

my_function()

print(" ------------------------- ")

# print(pb_local_a)
# it will give error like:
#  line 11, in <module>
#     print(pb_local_a)
#           ^^^^^^^^^^
# NameError: name 'pb_local_a' is not defined. Did you mean: 'pb_global_b'?

print(pb_global_b)