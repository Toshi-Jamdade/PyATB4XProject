# How to read a csv file

import  csv
with open("Testdata.csv") as csvfile:
    reader = csv.reader(csvfile)
    for col in reader:
        print(col[0],col[1], sep="|")


# username|password
# admin|admin
# admin|admin123
# admin|password
# admin|password123