import os

# operating system - files, path related to the OS

print(os.name)      #nt
if os.name == "posix":
    print("using mac")
else:
    print("using windows")
#nt - windows os

#####################################################################################

# print(os.getcwd())
# os.chdir("/Users/Toshi/Downloads")
# print(os.getcwd())
# C:\Users\Toshi\PycharmProjects\PyATB4XProject\src\11_class_of_10_September_Exceptions
# C:\Users\Toshi\Downloads

#####################################################################################

# os.mkdir('new_directory')

#####################################################################################

# os.makedirs('parent/child/grandchild')

#####################################################################################

# print(os.listdir('.'))
# ['1_Exceptions.py', 'Lab2.py', '3_Example.py', '4_Example.py', '5_Example.py', '6_Example.py', '7_Example.py', '8_.py', 'example.txt', 'new_directory', 'parent', '__init__.py']

##########################################################################

# for file in os.listdir('.'):
#     print(file)
#
# 1_Exceptions.py
# Lab2.py
# 3_Example.py
# 4_Example.py
# 5_Example.py
# 6_Example.py
# 7_Example.py
# 8_.py
# example.txt
# new_directory
# parent
# __init__.py

#####################################################################################

# os.remove('example.txt')

#####################################################################################

# os.rmdir('new_directory')

#####################################################################################

# os.rename('old_name.txt', 'new_name.txt')

# Following we will use generally
full_path = os.path.join('folder', 'file.txt')
print(full_path)
print(os.path.exists('file.txt'))
print(os.path.isdir('directory_name'))

#####################################################################################