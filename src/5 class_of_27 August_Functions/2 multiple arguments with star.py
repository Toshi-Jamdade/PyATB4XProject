def make_pizza(*toppings, base):
    print(toppings, base)

amit = make_pizza("mushroom", "paneer", "tomato", "onion", base="thin crust")

#('mushroom', 'paneer', 'tomato', 'onion') thin crust

# def make_pizza(*toppings, *base):  - 2 * are not allowed in a function, only 1 argument is allowed to have * multiple arguments

# def make_pizza2(base, *toppings):   - not allowed, * should be the first one if you have multiple arguments.
#     print(toppings, base)
# toshi = make_pizza2(base="crust", "tomato", "paneer", "onion")

