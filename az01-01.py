import pandas as pd


df = pd.read_csv('salaries (2).csv')
print(df.head(5))
print(df.info())
print(df.describe())