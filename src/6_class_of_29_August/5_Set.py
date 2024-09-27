#Set
# Collection of Unique items
# {} - parenthesis
# no duplicates allowed

list_of_unique_items = {1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4}
print(list_of_unique_items)         # {1, 2, 3, 4, 5, 6, 7}

list1 = [45.2, 33, 33, 45, 21]
set1 = set(list1)
print(set1)     # {33, 21, 45, 45.2}

set2 = {1, 2, 3}
set3 = {4, 5, 6}
my_set = set2.union(set3)
print(my_set)           #{1, 2, 3, 4, 5, 6}

set2 = {1, 2, 3, 4, 5}
set3 = {4, 5, 6}
my_set = set2.intersection(set3)
print(my_set)       #{4, 5}

my_set = set2.difference(set3)
print(my_set)       #{1, 2, 3}

my_set = set3.difference(set2)
print(my_set)       # {6}

subset = set3.issubset(set2)
print(subset)       # False

set3 = {1, 2, 9, 8, 7, 6}
set4 = {6, 7, 8}
subset = set4.issubset(set3)
print(subset)       # True

print(len(set3))        # 6

set3.add(100)
print(set3)     # {1, 2, 100, 6, 7, 8, 9}
#It will add anywhere, no indexing.

