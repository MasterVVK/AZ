import pandas as pd

# 1. Создание DataFrame с данными
data = {
    'Имя': ['Анна', 'Борис', 'Виктор', 'Галина', 'Дмитрий', 'Елена', 'Иван', 'Катерина', 'Леонид', 'Мария'],
    'Математика': [3, 4, 5, 4, 3, 5, 4, 4, 2, 4],
    'Физика': [5, 4, 4, 4, 4, 5, 4, 4, 4, 4],
    'Химия': [4, 4, 4, 4, 3, 5, 4, 4, 4, 4],
    'Биология': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    'Литература': [4, 4, 4, 4, 4, 5, 4, 4, 4, 4]
}

df = pd.DataFrame(data)

print("\n", df.describe(),"\n")

# 2. Вывод первых нескольких строк DataFrame
first_rows = df.head()
print("Первые несколько строк DataFrame:\n", first_rows)

# 3. Вычисление средней оценки по каждому предмету
mean_grades = df.mean(numeric_only=True)
print("\nСредние оценки по предметам:")
for subject, grade in mean_grades.items():
    print(f"{subject}: {grade:.2f}")

# 4. Вычисление медианной оценки по каждому предмету
median_grades = df.median(numeric_only=True)
print("\nМедианные оценки по предметам:")
for subject, grade in median_grades.items():
    print(f"{subject}: {grade:.2f}")

# 5. Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"\nQ1 для математики: {Q1_math}")
print(f"Q3 для математики: {Q3_math}")
print(f"IQR для математики: {IQR_math}")

# 6. Вычисление стандартного отклонения
std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение:")
for subject, grade in std_dev.items():
    print(f"{subject}: {grade:.2f}")
