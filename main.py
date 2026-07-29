import pandas as pd

# Загрузите набор данных из CSV-файла в DataFrame.
df = pd.read_csv('./Data/wcplayerstatistics.csv')

# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
print("df.head()")
print(df.head())

# Выведите информацию о данных (.info())
print("df.info()")
print(df.info())

# и статистическое описание (.describe()).
print("df.describe()")
print(df.describe())
