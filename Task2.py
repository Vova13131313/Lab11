import pandas as pd
import matplotlib.pyplot as plt

# Завантаження csv
df = pd.read_csv('comptagevelo2009.csv')

# Перевірка основних характеристик
print(df.head())
print(df.info())
print(df.describe())
print('='*15, '\n')

# Вивід даних
print("Загальна кількість велосипедистів за рік:", df['Berri1'].sum() + df['Maisonneuve_1'].sum() + df['Maisonneuve_2'].sum() + df['Brébeuf'].sum())
print("Загальна кількість велосипедистів за рік на Berri1:", df['Berri1'].sum())
print("Загальна кількість велосипедистів за рік на Maisonneuve_1:", df['Maisonneuve_1'].sum())
print("Загальна кількість велосипедистів за рік на Maisonneuve_2:", df['Maisonneuve_2'].sum())
print("Загальна кількість велосипедистів за рік на Brébeuf:", df['Brébeuf'].sum())

# Визначення найпопулярнішого місяця
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Month'] = df['Date'].dt.month
bike_columns = ['Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 'Brébeuf']
df['Total'] = df[bike_columns].sum(axis=1)
monthly_counts = df.groupby('Month')['Total'].sum()
most_popular_month_index = monthly_counts.idxmax()
max_cyclists = monthly_counts.max()
print(f"Статистика по місяцях:\n{monthly_counts}\n")
print(f"Найпопулярніший місяць (номер): {most_popular_month_index}")
print(f"Кількість велосипедистів у цьому місяці: {max_cyclists}")

# Побудова графіку
monthly_data = df.groupby('Month')[bike_columns].sum()
monthly_data.plot(kind='line', figsize=(10, 6), marker='o', linewidth=2)
plt.title('Завантаженість велодоріжок', fontsize=15)
plt.xlabel('Місяць', fontsize=12, color='red')
plt.ylabel('Кількість велосипедистів', fontsize=12, color='red')
plt.legend()
plt.grid(True)
plt.show()