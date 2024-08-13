"""
Задача 4. Продвинутая функция sum
Как вы знаете, в Python есть полезная функция sum,
которая умеет находить сумму элементов списков.
Иногда базовых возможностей функций не хватает для работы и приходится их усовершенствовать.
Напишите свою функцию sum, которая должна быть более гибкой, чем стандартная.
Она должна уметь складывать числа:
- из спска списков,
- набора параметров.
Основной код оставьте пустым или закомментированным (используйте его только для тестирования).
Примеры вызовов функции
> sum([[1, 2, [3]], [1], 3])
> Ответ в консоли: 10

> sum(1, 2, 3, 4, 5)
> Ответ в консоли: 15
"""


def my_sum(*args, summ=0) -> int:
    for elem in args:
        if isinstance(elem, int):
            summ += elem
        else:
            summ += my_sum(*elem)
    return summ


def my_sum_2(elem, *args):
    if elem is None:
        return 0
    if isinstance(elem, int):
        return elem + my_sum(*args)
    if isinstance(elem, list) or isinstance(elem, tuple):
        return my_sum(*elem) + my_sum(*args)
    raise TypeError('Wrong element type')


first_list = [[1, 2, [3]], [1], 3]
second_list = [1, 2, 3, 4, 5]
print(my_sum(first_list))
print(my_sum(second_list))
print(my_sum(1, 2, 4, 5))
print(my_sum_2(first_list))
print(my_sum_2(second_list))
print(my_sum_2(1, 2, 4, 5))
