
import pandas as pd
# оч прикольная библиотека 
# создание DataFrame из словаря
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)

# вывод DataFrame
print("Original DataFrame:")
print(df)
print()

# доступ к столбцам
print("Column 'Name':")
print(df['Name'])
print()

# выбор строк по индексу
print("Row with index 1:")
print(df.loc[1])
print()

# выбор определенных ячеек
print("Value at row 2, column 'Age':")
print(df.at[2, 'Age'])
print()

# добавление нового столбца
df['Salary'] = [50000, 60000, 70000]
print("DataFrame after adding 'Salary' column:")
print(df)

