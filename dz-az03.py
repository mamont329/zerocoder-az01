import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# 1. Гистограмма для случайных данных из нормального распределения
# ==========================================================

# Параметры нормального распределения
mean = 0          # среднее значение
std_dev = 1       # стандартное отклонение
num_samples = 1000  # количество образцов

# Генерация случайных чисел по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='steelblue', edgecolor='black')
plt.title('Гистограмма нормального распределения (mean=0, std=1)')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.3)

# ==========================================================
# 2. Диаграмма рассеяния для двух наборов случайных данных
# ==========================================================

# Два набора по 100 случайных чисел в диапазоне [0, 1)
x = np.random.rand(100)
y = np.random.rand(100)

plt.figure(figsize=(6, 6))
plt.scatter(x, y, color='crimson', alpha=0.6)
plt.title('Диаграмма рассеяния двух наборов случайных данных')
plt.xlabel('X (np.random.rand)')
plt.ylabel('Y (np.random.rand)')
plt.grid(alpha=0.3)

# Показать оба окна с графиками
plt.show()
