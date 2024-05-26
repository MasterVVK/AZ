import pandas as pd

# Создание DataFrame с категориальными данными
data = {
    'Имя': ['Анна', 'Борис', 'Виктор', 'Галина', 'Дмитрий'],
    'Пол': ['женский', 'мужской', 'мужской', 'женский', 'мужской'],
    'Оценка': ['хорошо', 'удовлетворительно', 'отлично', 'хорошо', 'удовлетворительно']
}

df = pd.DataFrame(data)
print(df.info())

# Преобразование столбцов в категориальные данные
df['Пол'] = df['Пол'].astype('category')
df['Оценка'] = df['Оценка'].astype('category')

# Вывод информации о DataFrame
print(df.info())

# Вывод первых строк DataFrame
print(df.head())

print(df['Пол'].cat.categories)
print(df['Пол'].cat.codes)
