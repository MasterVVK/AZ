import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
file_path = 'output-divan.csv'
data = pd.read_csv(file_path)

# Отображение первых нескольких строк данных
print("Первые строки данных:")
print(data.head())

# Проверка наличия столбца с ценами и очистка данных
if 'price' in data.columns:
    # Преобразование цен к числовому типу данных (если необходимо)
    data['price'] = pd.to_numeric(data['price'], errors='coerce')

    # Удаление строк с отсутствующими значениями в столбце цены
    data = data.dropna(subset=['price'])

    # Вычисление средней цены
    average_price = data['price'].mean()
    print(f"Средняя цена диванов: {average_price:.2f} рублей")

    # Построение гистограммы цен
    plt.figure(figsize=(10, 6))
    plt.hist(data['price'], bins=30, edgecolor='black', alpha=0.7)
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (рубли)')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.show()
else:
    print("Столбец 'price' не найден в данных.")
