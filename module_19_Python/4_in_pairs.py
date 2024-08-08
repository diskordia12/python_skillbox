"""
Задача 4. По парам
Напишите программу, которая инициализирует список из 10 случайных целых чисел,
а затем делит эти числа на пары кортежей внутри списка. Выведите результат на экран.
Дополнительно: решите задачу несколькими способами.

Пример:
> Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
> Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
"""
import random

original_list = [random.randint(0, 10) for _ in range(10)]
print(f'original_list: {original_list}')

modified_list = [(original_list[i], original_list[i + 1]) for i in range(0, 10, 2)]

print(f'modified list: {modified_list}')

print('\nAnother way')
# two_modified_list = [(num1, num2) for num1, num2 in zip(original_list[:: 2], original_list[1:: 2])]
two_modified_list = [num_pair for num_pair in zip(original_list[:: 2], original_list[1:: 2])]

print(f'Modified list produced with zip and slice: {two_modified_list}')
