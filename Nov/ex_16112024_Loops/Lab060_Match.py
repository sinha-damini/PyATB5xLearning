# Match Statement ->
# Switch in Java
# match the op and execute
# Python > 3.10

# match variable:
# case pattern1:
# code block
# case pattern2:
# code block

# Write a program to ask the user which browser he want to run automation.

browser_name = input("Enter the Browser Name\n")
match browser_name:
    case "firefox":
        print("Starting Firefox!!!!")
    case "chrome":
        print("Execute the Chrome code")
    case "edge":
        print("Execute the Edge code")
    case "safari":
        print("Execute the Safari code")
    case _:                             # _ -> nothing match: default
        print("Browser not found.")