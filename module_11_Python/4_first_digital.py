print('Задача 4. Первая цифра')

# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки.
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками

x = float(input('Enter number: '))

print(f'The first digital after point is {int((x - int(x)) * 10)}')

# Second way

from math import floor
d = floor(x * 10) % 10
