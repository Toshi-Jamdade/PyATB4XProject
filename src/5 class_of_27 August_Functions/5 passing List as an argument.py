
my_shopping_list = ["bread", "butter", "milk"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_food(my_shopping_list):
    my_shopping_list.append("cheese")
    more_item = input("Enter the item: ")
    my_shopping_list.append(more_item)
    my_shopping_list.insert(1, "jam")
    #my_shopping_list.remove(more_item)
    return my_shopping_list

l = bring_more_food(my_shopping_list)
print(l)

# bread
# 3
# Enter the item: paneer
# ['bread', 'jam', 'butter', 'milk', 'cheese', 'paneer']
