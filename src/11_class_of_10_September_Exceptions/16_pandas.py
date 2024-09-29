#Read csv file

import pandas as pd

df = pd.read_csv("Testdata.csv")
print(df)

#   username     password
# 0    admin        admin
# 1    admin     admin123
# 2    admin     password
# 3    admin  password123