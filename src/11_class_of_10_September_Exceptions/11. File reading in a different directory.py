import os

full_path_of_file = os.path.join("/Users/Toshi/PycharmProjects/PyATB4XProject/src/11_class_of_10_September_Exceptions/Toshi", 'test.txt')

file = open(full_path_of_file, 'r')
content = file.read()
print(content)

