import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Установка начальной точки для генерации случайных чисел (для воспроизводимости)
np.random.seed(42)

# Создание временных меток
date_rng = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Генерация случайных данных
data = np.random.randn(len(date_rng))

# Создание временного ряда с помощью Pandas
time_series = pd.Series(data, index=date_rng)

# Визуализация временного ряда
plt.figure(figsize=(10, 6))
plt.plot(time_series, label='Случайные данные')
plt.title('Временной ряд')
plt.xlabel('Дата')
plt.ylabel('Значение')
plt.legend()
plt.show()

# Ресемплинг временного ряда по месяцам
monthly_resampled = time_series.resample('ME').mean()

# Визуализация ресемплированного временного ряда
plt.figure(figsize=(10, 6))
plt.plot(monthly_resampled, label='Ресемплированные данные (по месяцам)', color='orange')
plt.title('Временной ряд (Ресемплированный по месяцам)')
plt.xlabel('Дата')
plt.ylabel('Среднее значение')
plt.legend()
plt.show()
