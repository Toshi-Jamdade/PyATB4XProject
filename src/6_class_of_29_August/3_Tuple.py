#List is mutable in nature
#mutable means change

squares = [1, 4, 9, 16, 25]
squares[3] = 64
print(squares)      # [1, 4, 9, 64, 25]

#Tuple - Collection of items (Duplicate is allowed).
# round brackets "()" are used to store tuple items.
# Tuple is immutable in nature
# Uses less memory
# Fixed data

my_tuple = (1, 4, 9, 16, 25)
# my_tuple[3] = 64        # Tuple is immutable in nature
# print(my_tuple)     #TypeError: 'tuple' object does not support item assignment
print(my_tuple)         # (1, 4, 9, 16, 25)

squares = tuple(squares)        #conversion of list to tuple
print(squares)          # (1, 4, 9, 64, 25)

my_tuple = list(my_tuple)       #conversion of tuple to list
print(my_tuple)         #[1, 4, 9, 16, 25]


hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
new_tuple = (hero1, hero2)          #tuple within tuple
print(new_tuple)        #(('Batman', 'Bruce Wayne'), ('Wonder Woman', 'Diana Prince'))
print(new_tuple[0])     #('Batman', 'Bruce Wayne')
print(new_tuple[0][0])      #Batman
print(new_tuple[1][1])      #Diana Prince

