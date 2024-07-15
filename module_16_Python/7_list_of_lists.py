"""
Задание 7. Список списков
Дан многомерный список:
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
Напишите код, который раскрывает все вложенные списки, то есть оставляет лишь внешний список.
Для решения используйте только list comprehensions.
Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
"""


def create_list(user_list: list) -> list:
    easy_list = []
    for elem in user_list:
        if type(elem) != list:
            easy_list.append(elem)
        else:
            easy_list.extend(create_list(elem))
    return easy_list


nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

print('Way with recursion:')
print(create_list(nice_list))

print('\nWay with list comprehension: ')
new_list = [num for group in nice_list
                for small_group in group
                for num in small_group]

print(new_list)
