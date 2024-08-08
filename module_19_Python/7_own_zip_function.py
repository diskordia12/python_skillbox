"""
Задача 7. Своя функция zip
В самом конце собеседования вам неожиданно сказали: «Расскажите, что делает функция zip».
Чтобы произвести впечатление, вы решили не только рассказать о ней, но и написать её аналог.

Даны строка и кортеж из чисел.
Напишите программу, которая создаёт генератор из пар кортежей «символ — число».
Затем выведите на экран сам генератор и кортежи.

Пример:
> Строка: abcd
> Кортеж чисел: (10, 20, 30, 40)

> Результат:
> <generator object <genexpr> at 0x00000204A4234048>
> ('a', 10)
> ('b', 20)
> ('c', 30)
> ('d', 40)

Дополнительно: создайте полный аналог функции zip — сделайте так, чтобы программа работала
с любыми итерируемыми типами данных.

Подсказка
Ранее мы проходили List comprehensions — по сути, генератор списка.
В этом случае, чтобы создать генератор, попробуйте поэкспериментировать с генератором списка.

Пример:
print([i for i in range(10)])
print((i for i in range(10)))
"""


def my_zip(text: str, numbers: tuple):
    return ((text[i], numbers[i]) for i in range(min(len(text), len(numbers))))


from typing import Sequence


def custom_zip(it1: Sequence, it2: Sequence):
    return ((it1[i], it2[i]) for i in range(min(len(it1), len(it2))))


text = 'abcd'
numbers = (10, 20, 30, 40)


print(my_zip(text, numbers))
print(list(my_zip(text, numbers)))

for pair in my_zip(text, numbers):
    print(pair)

