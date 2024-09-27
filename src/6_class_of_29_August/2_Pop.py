squares = [1, 4, 9, 16, 25]
#squares = [1, 4, 9, 16, 25, "Praod"]
#print(squares.sort(reverse=False))      #TypeError: '<' not supported between instances of 'str' and 'int'

squares.sort(reverse=type)
print(squares)      # [25, 16, 9, 4, 1]

squares.pop()       #remove & return item at index (default last).
print(squares)      # [25, 16, 9, 4]

print(squares.pop())        # 4
print(squares)              # [25, 16, 9]

squares.pop(1)
print(squares)      # [25, 9]