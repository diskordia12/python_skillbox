"""
Задача 5. Функция сортировки
Напишите функцию, которая сортирует по возрастанию кортеж,
состоящий из целых чисел, и возвращает его отсортированным.
Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.

Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

Пример вызова функции:
> tpl = (6, 3, -1, 8, 4, 10, -5)
> print(tpl_sort(tpl))
> Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)
"""


def tpl_sort(numbers: tuple) -> tuple:
    if any(not isinstance(num, int) for num in numbers):
        return numbers
    # if all(isinstance(num, int) for num in numbers):
    #     return tuple(sorted(numbers))
    # for num in numbers:
    #     if not isinstance(num, int):
    #         return numbers

    return tuple(sorted(numbers))


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))
tpl = (6, 3, -1, 8, 4, 10.7, -5)
print(tpl_sort(tpl))

