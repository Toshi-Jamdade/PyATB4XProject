import pandas as pd

def readCSV():
    df = pd.read_csv("Testdata.csv")
    print(df)
    print("I'm reading the excel file")