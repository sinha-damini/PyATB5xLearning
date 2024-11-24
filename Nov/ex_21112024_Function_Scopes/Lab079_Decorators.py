# @add_extra_security
# def drivinig_scooty():
#     print("Normal Function!!")
#     print("I am driving a scooty.")

#Will give error as name 'add_extra_security' is not defined yet.
# So, first we have to define the Decorator.

def add_extra_security(func):

    def wrapper():
        print("1.Before the function is called.")
        print("2.Add Helmet, Dashcash, Gloves, Knee Guards, License")
        func()#driving_scooty()
        print("3.After the function is called.")
        print("4.Secure Driving, Leave all the items.")
    return wrapper()


@add_extra_security
def drive_ola_scooter():
    print("Ola")
@add_extra_security
def drivinig_scooty():
    print("Normal Function!!")
    print("I am driving a scooty.")
