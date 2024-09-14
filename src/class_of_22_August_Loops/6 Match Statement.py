#Match Statement
#Switch in JAVA
# match the op and execute
# Match works only in Python version > 3.10
from idlelib.browser import browseable_extension_blocklist

#Syntax:
#match variable:
    #case pattern1:
        #code block
    #case pattern2:
        #code block
    #case _:           # _ is the default if no other case matches
        #code block

#Write a program to ask the user which browser he want to run automation
browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox code")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("Browser not found")