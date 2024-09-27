a, b, c = (10, 11, 12)
print(a)
print(b)
print(c)

#Search in Tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)        #True
print("New Delhi" in cities)       #False

t = (12, 34, 56)
#t.append(14)    #AttributeError: 'tuple' object has no attribute 'append'
print(t)        #(12, 34, 56)

my_list = list(t)
my_list.append(14)
t = tuple(my_list)
print(t)        #(12, 34, 56, 14)

my_new_tuple = t + (5,)
print(my_new_tuple)     #(12, 34, 56, 14, 5)

