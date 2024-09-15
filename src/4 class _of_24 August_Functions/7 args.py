# *args = multiple arguments with no limit, -> list

def print_arguments(*args):
    print(args[0])

print_arguments("Toshi", "Amit", "Lucky")
print_arguments("a", "b")
print_arguments(1, "test", 900, 895)
print_arguments("abcd", 8765, True, False, "Toshi")
#print_arguments()   - will give error because minimum 1 argument is required

# Toshi
# a
# 1
# abcd

def print_arguments(*args):
    for i in args:
        print(i)

print_arguments("Toshi", "Amit", "Lucky")
print_arguments("a", "b")
print_arguments(1, "test", 900, 895)
print_arguments("abcd", 8765, True, False, "Toshi")
# Toshi
# Amit
# Lucky
# a
# b
# 1
# test
# 900
# 895
# abcd
# 8765
# True
# False
# Toshi