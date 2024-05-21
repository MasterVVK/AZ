import pandas as pd


df = pd.read_csv('dz.csv')
#print(df.head(5))
#print(df.info())
#print(df.describe())

print(df.groupby('City')['Salary'].mean())
