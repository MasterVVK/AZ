import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
#print(s)

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
#print(df)


df = pd.read_csv('World-happiness-report-2024.csv')
print(df.info())
print(df.describe())
print(df[['Country name', 'Regional indicator']])
print(df.loc[56])
print(df.loc[56, 'Healthy life expectancy'])