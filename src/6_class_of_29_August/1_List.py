# List:
# List is Collection of items (Duplicate is allowed).
# square brackets "[]" are used to store list items.
#List is mutable in nature
# More memory
# dynamic data

mylist = [1, 2, 3]      #same type of data
mylist2 = ["Toshi", 1, 800, 15.8, True]         #different type of data

print(mylist)       #[1, 2, 3]
print(len(mylist))      #3
print(mylist[0])        #1
#print(mylist[10])       #IndexError: list index out of range
print(mylist[2])        #3

# [1, 2, 3]
# 3
#1
#3

mylist[0] = "Testing"
# mylist[10] = "QA"       #IndexError: list assignment index out of range

#Indexing:
print("Element at the index 0 is", mylist[0])   # Element at the index 0 is Testing

print(mylist)       #['Testing', 2, 3]

for element in mylist:
    print(element)
# Testing
# 2
# 3


#Append - adds to the end of the list
mylist.append(4)
print(mylist)                #['Testing', 2, 3, 4]
# mylist.append(5, 6, 7)        #not allowed to append multiple at a time

#Extend - to add multiple items at a time
mylist.extend([8, 9, 10])
print(mylist)                   #['Testing', 2, 3, 4, 8, 9, 10]
mylist.extend([11])
print(mylist)                   #['Testing', 2, 3, 4, 8, 9, 10, 11]

#insert - to add in between of a list
mylist.insert(1, "Notes")
print(mylist)                   #['Testing', 'Notes', 2, 3, 4, 8, 9, 10, 11]
print(len(mylist))              #9

mylist.insert(-1, "Lily")
print(mylist)                   #['Testing', 'Notes', 2, 3, 4, 8, 9, 10, 'Lily', 11]

#remove()
mylist.remove("Notes")
print(mylist)                   #['Testing', 2, 3, 4, 8, 9, 10, 'Lily', 11]

#copy
my_copy_list = mylist.copy()
print(mylist)
print(my_copy_list)
# ['Testing', 2, 3, 4, 8, 9, 10, 'Lily', 11]
# ['Testing', 2, 3, 4, 8, 9, 10, 'Lily', 11]

#clear
mylist.clear()
print(mylist)
print(my_copy_list)
# []
# ['Testing', 2, 3, 4, 8, 9, 10, 'Lily', 11]

my_copy_list.remove("Testing")
my_copy_list.remove("Lily")
print(my_copy_list)             #[2, 3, 4, 8, 9, 10, 11]

my_copy_list.extend([1, 0, 5])
print(my_copy_list)             #[2, 3, 4, 8, 9, 10, 11, 1, 0, 5]

#Sort   - Only integers & floats can be sorted, str cannot be sorted
my_copy_list.sort()
print(my_copy_list)             #[0, 1, 2, 3, 4, 5, 8, 9, 10, 11]

#Reverse
my_copy_list.reverse()
print(my_copy_list)             #[11, 10, 9, 8, 5, 4, 3, 2, 1, 0]

my_copy_list.sort()
print(my_copy_list)             #[0, 1, 2, 3, 4, 5, 8, 9, 10, 11]

my_copy_list.sort(reverse=True)
print(my_copy_list)              #[11, 10, 9, 8, 5, 4, 3, 2, 1, 0]

l1 =[1,2,3]
l2 = [4,5,6]
l3 = l1+l2
print(l3)                   #[1, 2, 3, 4, 5, 6]







