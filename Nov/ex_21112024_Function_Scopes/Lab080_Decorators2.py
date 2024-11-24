# def add_before_ui_after_ui(func):
def add_before_ui_after_ui(test_ui):

    def wrapper():
        print("Before the running UI TC")
        print("Start the Browser ")
        # func()
        test_ui()
        print("Ending the running UI TC")
        print("Quit the Browser!")
    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print(">> I will Test the UI <<")


print(">>>>>>>>>>>>Printing Without Decorator<<<<<<<<<<<<<<<<<<<<<")

def start():
    print("Before the running UI TC")
    print("Start the Browser ")

def end():
    print("Ending the running UI TC")
    print("Quit the Browser!")

def test_ui():
    print(">> I will Test the UI <<")

start()
test_ui()
end()