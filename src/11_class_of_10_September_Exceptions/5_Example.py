import os

# file = open('example.txt', 'r')
# print(file.read())

full_path = os.getcwd()
print(full_path)
full_path_file = full_path + "/example.txt"
print(full_path_file)
file = open(full_path_file, 'r')
print(file.read())




