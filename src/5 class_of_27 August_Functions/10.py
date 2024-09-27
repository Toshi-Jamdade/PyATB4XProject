#__init__.py

# create dir - normal folder - python doesn't serach the files here or code here.


# folder with file __int__.py - python will search the code here
# __init__.py -> dir -> module (where python will search better)

# e.g:
# # from src.ex_27082024.normal_dir import sum_91   #This will not work becoz, __init__.py is not present in the folder
# from src.Aug.ex_27082024.python_package.Lab092 import sum_two     #This will work becoz, __init__.py is present in the folder
#
# op = sum_two(3, 4)
# print(op)

