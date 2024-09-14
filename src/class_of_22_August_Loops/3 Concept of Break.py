#break - based on the condition, exit the loop

for i in range(0, 10):
    print(i, end=" ")
    if i == 5:
        break
# 0 1 2 3 4 5

print("\n")

for i in range(10):
    print(i, end=" ")       #0 1 2 3 4 5 6 7 8 9

print("\n")

for j in range(0, 5, 1):
    if j == 2:
        print(j)
    else:
        print("No o/p")
#No o/p
#No o/p
#2
#No o/p
#No o/p


for k in range(0, 10, 1):
    if k == 6 or k == 5:
        print(k)
    else:
        pass        #pass - it is used to pass - means no output