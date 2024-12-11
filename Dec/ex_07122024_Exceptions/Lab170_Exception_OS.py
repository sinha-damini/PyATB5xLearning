import os

print(os.getcwd())
# Returns the current working directory

# List files in the current directory
files = os.listdir('/Users/HP/PycharmProjects/PyATB5xLearning/')
print(f"Files in current directory: {files}")

# Create a new directory
# os.mkdir('Test2')

#Remove a directory.
# It will throw a Permission error; that's why we have to change the current working directory.
# os.rmdir("/Users/HP/PycharmProjects/PyATB5xLearning/Dec/ex_07122024_Exceptions/Test2")
# os.chdir("..")
# os.rmdir("Test2")

# Check if a file exists
file_exist = os.path.exists("Lab162_Exception.py")
print(file_exist)

print(os.name) # posix == mac, nt - windows
