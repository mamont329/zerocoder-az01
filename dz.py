import pandas as pd

# используйте файл приложенный к дз - dz.csv
df = pd.read_csv('./Data/dz.csv')

#print("df.head()")
#print(df.head())

# Определите среднюю зарплату (Salary) по городу (City)
group = df.groupby('City')['Salary']
print('Средняя зарплата (Salary) по городу (City)')
print(group.mean())