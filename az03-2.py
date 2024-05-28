import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 1000  # Количество образцов
x_data = np.random.rand(num_samples)
y_data = np.random.rand(num_samples)

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, alpha=0.5, edgecolors='w', linewidth=0.5)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')
plt.grid(True)
plt.show()
