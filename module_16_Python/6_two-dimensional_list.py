"""
Задание 6. Двумерный список
Часто в программировании приходится писать код исходя из результата,
который требует заказчик. В этот раз ему нужно получить двумерный список:
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
Напишите программу, которая генерирует такой список и выводит его на экран.
Используйте только list comprehensions.
"""

# 1 2 3 4 5 6 7 8 9 10 11 12
#
# [0 4 8]
# [1 5 9]
# [2 6 10]
# [3 7 11]


# def create_list(num: int) -> list:
#     return [n for n in range(num, num + 12, 4)]
#
#
# result = [create_list(l) for l in range(1, 5)]
# print(result)


def create_list(num: int) -> list:
    return [num + 4*i for i in range(0, 3)]


result = [create_list(l) for l in range(0, 4)]
print(result)