with open("Toshi.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")