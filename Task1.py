import pandas as pd
import random

# Дані
data = {
    "Name": ["Engine 1", "Engine 2", "Engine 3", "Engine 4", "Engine 5", "Engine 6", "Engine 7", "Engine 8", "Engine 9", "Engine 10"],
    "Power": [random.randint(50, 150), random.randint(50, 150), random.randint(50, 150), random.randint(50, 150), random.randint(50, 150), random.randint(50, 150), random.randint(50, 150), random.randint(50, 150), random.randint(50, 150), random.randint(50, 150)],
    "Price": [random.randint(1000, 10000), random.randint(1000, 10000), random.randint(1000, 10000), random.randint(1000, 10000), random.randint(1000, 10000), random.randint(1000, 10000), random.randint(1000, 10000), random.randint(1000, 10000), random.randint(1000, 10000), random.randint(1000, 10000)]
}
df = pd.DataFrame(data)

# Вивід інформації початкового датафрейму
print(f"Весь датафрейм:\n{df}\n")
print(f"3 перші рядки:\n{df.head(3)}\n")
print(f"Типи даних:\n{df.dtypes}\n")
print(f"Кількість рядків і стопвців: {df.shape}\n")
print(f"Описова статистика:\n{df.describe()}\n")

# Нова колонка релевантності, сортування за нею та її середнє значення
df['Relevance'] = df['Power'] / df['Price']
df_sorted = df.sort_values(by='Relevance', ascending=False)
print(f"Весь датафрейм, відсортований по релевантності (потужність / ціна):\n{df_sorted}\n")
print(f"Середня релевантність:", df['Relevance'].mean())

# Максимальна потужність та мінімальна ціна
max_power_name = df.loc[df['Power'].idxmax(), 'Name']
min_price_name = df.loc[df['Price'].idxmin(), 'Name']
print(f"Двигун з максимальною потужністю: {max_power_name} ({df['Power'].max()})")
print(f"Двигун з мінімальною ціною: {min_price_name} ({df['Price'].min()})")