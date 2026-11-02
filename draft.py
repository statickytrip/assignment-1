import pandas as pd

# load the data file (not the raw)
df = pd.read_csv("data/insurance.csv")

# check is there are empty values > output 0 in all categories
print(df.isnull().sum())



