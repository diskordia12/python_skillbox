"""
Задача 1. Кубы и квадраты
Пользователь вводит числа A и B. Напишите программу, которая генерирует два списка:
в первом лежат кубы чисел в диапазоне от А до В, во втором — квадраты чисел в этом же диапазоне.
Выведите списки на экран. Для генерации используйте list comprehensions (как и в следующих задачах).

Пример:
> Левая граница: 5
> Правая граница: 10
> Список кубов чисел в диапазоне от 5 до 10: [125, 216, 343, 512, 729, 1000]
> Список квадратов чисел в диапазоне от 5 до 10: [25, 36, 49, 64, 81, 100]
"""
import random

# left_border = int(input('Left border: '))
# right_border = int(input('Right border: '))
#
# cube_numbers = [x ** 3 for x in range(left_border, right_border + 1)]
# square_numbers = [x ** 2 for x in range(left_border, right_border + 1)]
# print(f'List of cubes of numbers from {left_border} to {right_border}: {cube_numbers}')
# print(f'List of square of numbers from {left_border} to {right_border}: {square_numbers}')

"""
Задача 2. Сообщение
Илья решил безобидно подшутить над другом и написал программу для смартфона,
которая при отправке сообщения удваивает каждый символ строки и заодно к каждому удвоенному
добавляет ещё один дополнительный.
Пользователь вводит строку и дополнительный символ.
Напишите программу, которая генерирует два списка: в первом списке каждый элемент — 
удвоенная буква первой строки, во втором списке каждый элемент — конкатенация элемента
первого списка и дополнительного символа.

Пример:
> Введите строку: привет
> Введите дополнительный символ: !
> Список удвоенных символов: ['пп', 'рр', 'ии', 'вв', 'ее', 'тт']
> Склейка с дополнительным символом: ['пп!', 'рр!', 'ии!', 'вв!', 'ее!', 'тт!']
"""

# user_message = input('Enter a message: ')
# symbol = input('Enter a symbol: ')
# double_symbols = [sym * 2 for sym in user_message]
# symbols_with_additional_sym = [sym + symbol for sym in double_symbols]
# print(f'List of double symbols: {double_symbols}')
# print(f'List with additional symbol: {symbols_with_additional_sym}')


"""
Задача 3. Повышение цен
Дан список цен на пять товаров с точностью до копейки.
Так как экономика даёт о себе знать, мы спрогнозировали, что через год придётся повышать цены
на X процентов, а ещё через один год — ещё на Y процентов.
Напишите программу, которая получает на вход список цен на товары
(вещественные числа, список генерируется также с помощью list comprehensions)
и выводит в одну строку общую сумму стоимости товаров за каждый год.

Пример:
> Цена на товар: 1.09
> Цена на товар: 23.56
> Цена на товар: 57.84
> Цена на товар: 4.56
> Цена на товар: 6.78
> Повышение на первый год: 0
> Повышение на второй год: 10
> Сумма цен за каждый год: 93.83 93.83 103.21
"""


# def get_higher_price(percent: float, price: float) -> float:
#     return round(price * (1 + percent / 100), 2)
#
#
# prices = [float(input('Price for item: ')) for _ in range(5)]
# first_increase = float(input('Price increase for the first year (%): '))
# second_increase = float(input('Price increase for the second year (%): '))
# first_prices = [get_higher_price(first_increase, price) for price in prices]
# second_prices = [get_higher_price(second_increase, price) for price in first_prices]
# print(f'Sum for the each year: 1 - {round(sum(prices), 2)}, 2 - {round(sum(first_prices), 2)}, 3 -{round(sum(second_prices), 2)}')

"""
Задача 1. Список чётных чисел
Пользователь вводит два числа: А и В.
Реализуйте код, который генерирует список из чётных чисел в диапазоне от А до B.
Используйте list comprehensions (как и в следующих задачах).
"""
# a = int(input('a: '))
# b = int(input('b: '))
# even_numbers = [num for num in range(a, b + 1) if num % 2 == 0]
# print(f'Even numbers: {even_numbers}')

"""
Задача 2. Магазин
У нас есть вот такой список цен на некоторые товары из магазина:
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
В этом списке также хранятся цены на товары, которые уже давно не продаются.
По какой-то причине система, вместо того чтобы их занулить, просто приписала к ним минус.
Нам нужно это исправить.
Напишите программу, которая генерирует новый список из первого списка,
заменяя все отрицательные числа на ноль.
Результат:
> [1.25, 0, 10.22, 3.78, 0, 1.16]
"""
# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# right_prices = [(price if price > 0 else 0) for price in original_prices]
# print(f'New prices: {right_prices}')

"""
Задача 3. Отряды
Мы продолжаем пробовать себя в качестве разработчика игр.
Теперь нужно написать небольшую логику поведения некоторых отрядов,
а также их урон. Есть два отряда, в каждом по 10 монстров.
В первом отряде у каждого монстра урон абсолютно случайный и колеблется от 50 до 80,
а во втором — от 30 до 60. Оба отряда вместе напали на третий, также из 10 юнитов.
Юнит третьего отряда погибает, если сумма урона от двух монстров больше 100.
Напишите программу, которая генерирует случайные значения в первых двух списках
в заданных диапазонах, а также генерирует список, состоящий из фраз «Погиб» или «Выжил».
Выведите все списки на экран.
Пример:
> Урон первого отряда: [77, 75, 76, 77, 76, 73, 57, 67, 76, 52]
> Урон второго отряда: [53, 51, 31, 60, 49, 37, 31, 60, 37, 47]
> Состояние третьего отряда: ['Погиб', 'Погиб', 'Погиб', 'Погиб', 'Погиб', 'Погиб', 'Выжил', 'Погиб', 'Погиб', 'Выжил']
"""

first_squad = [random.randint(50, 80) for _ in range(10)]
second_squad = [random.randint(30, 60) for _ in range(10)]
third_squad_conditions = [('died' if first_squad[i_damage] + second_squad[i_damage] > 100
                           else 'survived')
                           for i_damage in range(10)]
print(f'First squad: {first_squad}')
print(f'Second squad: {second_squad}')
print(f'Condition of third squad: {third_squad_conditions}')
