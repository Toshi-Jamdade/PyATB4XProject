# Loops - To repeat a block of code multiple times

# Python has 2 Loops:
# For Loop
# While Loop

#Keywords:
# Break
# Continue

# Print Hello 10 times

# for loop
# syntax:
#for variable name in range (start, stop, step):

# Range(start, stop-1, step)
# range(0, 10, 1)
# range(0,10)
# range(10)     #by default start will be taken as 0

for i in range (1, 10):     #1 to 9
    print(i)

print("\n")

for j in range (1, 10, 3):      #1,4,7
    print(j)

print("\n")

for number in range(10, 0, -2):     #10, 8, 6, 4, 2
    print(number)

print("\n")

for test in range(0, 10, -2):       #Nothing will print
    print(test)




