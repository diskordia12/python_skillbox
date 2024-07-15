"""
Задание 8. Сортировка
Что нужно сделать
Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию
и выводит их на экран. Дополнительный список использовать нельзя.
Также нельзя использовать готовые функции sorted/min/max и метод sort
Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.

Пример:
Изначальный список: [1, 4, –3, 0, 10]
Отсортированный список: [–3, 0, 1, 4, 10]
"""

"""
Bubble sort
"""


def sorting(numbers: list) -> list:
    for i in range(len(numbers) - 1):
        swap = False
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                # switch swap if elem exchanged
                swap = True
        # Stop cycle, if there wasn't exchanged
        if not swap:
            break
    return numbers

#
# size = int(input('Enter size of your list: '))
#
# numbers = list()
# numbers = [int(input('Enter a number: ')) for num in range(size)]
# bubble_sorted_numbers = sorting(numbers)
# print(f'Sorted list: {bubble_sorted_numbers}')


"""
Merge sort
"""


def merge_list(first_list: list, second_list: list) -> list:
    union_list = list()
    i, j = 0, 0
    if not first_list:
        union_list = second_list
        return union_list

    if not second_list:
        union_list = first_list
        return union_list

    while i < len(first_list) and j < len(second_list):
        if first_list[i] < second_list[j]:
            union_list.append(first_list[i])
            i += 1
        elif second_list[j] < first_list[i]:
            union_list.append(second_list[j])
            j += 1
        else:
            union_list.append(first_list[i])
            i += 1
            second_list.remove(second_list[j])

    union_list.extend(second_list[j:] if i > j else first_list[i:])

    return union_list


def simple_sort(numbers: list) -> list:
    if len(numbers) == 2:
        if numbers[0] > numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
    return numbers


def merge_sorting(numbers: list) -> list:
    if len(numbers) <= 2:
        return simple_sort(numbers)

    middle = len(numbers) // 2
    left_list = merge_sorting(numbers[:middle])
    right_list = merge_sorting(numbers[middle:])
    return merge_list(left_list, right_list)


size = int(input('Enter size of your list: '))
numbers = list()
numbers = [int(input('Enter a number: ')) for num in range(size)]
bubble_sorted_numbers = sorting(numbers)
print(f'Sorted list by bubble sorting: {bubble_sorted_numbers}')

merge_sorted_numbers = merge_sorting(numbers)
print(f'Sorted list by merge sorting: {merge_sorted_numbers}')