import os
try:
    file = open('testdata.txt', 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("File not found, fix the path or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
