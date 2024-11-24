public_toilet = "Public"

def home():
    private_toilet = "Private"
    public_toilet = "Local Public"
    print(public_toilet)
    print(private_toilet)

def stranger():
    print(public_toilet)
    # will print 'Public' as global varibale will be taken
    # print(private_toilet)
    # #NameError: name 'private_toilet' is not defined

home()
stranger()

print(public_toilet)
#will print 'Public' as global varibale will be taken
#print(private_toilet)
# #NameError: name 'private_toilet' is not defined