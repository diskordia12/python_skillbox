"""
Задание 2. Уникальное объединение списков
Контекст
Вы работаете в команде разработки программного обеспечения для компании, которая занимается
обработкой и анализом данных. Ваша команда получает данные из различных источников,
вам нужно объединить их в один отсортированный список для дальнейшей обработки
Однако источники данных возвращают отсортированные списки с возможными дубликатами,
и ваша задача — создать программу, которая объединит эти списки в один отсортированный
список без дубликатов.

Задача
Напишите программу, которая объединяет два отсортированных списка целых чисел
в один отсортированный список без дубликатов.

Пример:
> list1 = [1, 3, 5, 7, 9]
> list2 = [2, 4, 5, 6, 8, 10]
> merged = merge_sorted_lists(list1, list2)
> print(merged)
> Вывод в консоли:
> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Советы
Учтите, что один список может быть короче другого.
Проверьте ваше решение с различными тестовыми данными, включая случаи с пустыми списками,
списками без дубликатов и списками с повторяющимися элементами.
Требование отсутствия дубликатов значительно усложняет задачу.
Убедитесь, что в вашем итоговом списке дубликатов не будет.

"""


def merge_sorted_list(first_list: list, second_list: list) -> list:
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
    # Without ternary operator
    # if i > j:
    #     union_list.extend(second_list[j:])
    # else:
    #     union_list.extend(first_list[i:])

    return union_list



"""
This is definetely the optimal way, but for the sake of education here is less effective
but also less code way
> first_list = list(set(first_list + second_list))
> first_list.sort()
"""

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 7, 8, 10]


merged = merge_sorted_list(list1, list2)
print(f'Merged list: {merged}')


