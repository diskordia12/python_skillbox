"""
Задание 7. Три списка
Даны три списка.
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

Нужно выполнить две задачи:
- найти элементы, которые есть в каждом списке;
- найти элементы из первого списка, которых нет во втором и третьем списках.
Каждую задачу нужно выполнить двумя способами:
- без использования множеств;
- с использованием множеств.
Пример выполнения на других данных:
array_1 = [1, 2, 3, 4]
array_2 = [2, 4]
array_3 = [2, 3]
Вывод:
Задача 1:
Решение без множеств: 2
Решение с множествами: 2
Задача 2:
Решение без множеств: 1
Решение с множествами: 1
"""

# array_1 = [1, 2, 3, 4]
# array_2 = [2, 4]
# array_3 = [2, 3]

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

array_1_set = set(array_1)
array_2_set = set(array_2)
array_3_set = set(array_3)

print('Solution with sets')
print(f'elements that are in every list: '
      f'{array_1_set.intersection(array_2_set).intersection(array_3_set)}')

print(f'\nelements from the first list that are not in the second and third lists: '
      f'{array_1_set.difference(array_2_set).difference(array_3_set)}')

print('\nSolution without sets')
result_1 = list()
for elem in array_1:
    if elem in array_2 and elem in array_3:
        result_1.append(elem)

print(f'elements that are in every list: {result_1}')

result_2 = list()
for elem in array_1:
    if elem not in array_2 and elem not in array_3:
        result_2.append(elem)

print(f'\nelements from the first list that are not in the second and third lists: '
      f'{result_2}')
