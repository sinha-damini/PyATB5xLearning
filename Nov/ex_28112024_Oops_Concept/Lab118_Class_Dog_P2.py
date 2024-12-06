class Dog:
    # A
    name = "Chow"
    # it is not a proper way, as for every obj name would be "Chow".L
    breed = None
    height = None
    weight = None

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass


# Object Ref
chow_ref = Dog()
mow_ref = Dog()

print(chow_ref.name)
print(mow_ref.name)