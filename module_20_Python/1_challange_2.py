"""
Задача 1. Challenge-2
Вдохновившись мотивацией Антона, ваш друг тоже решил поставить перед собой задачу,
но не напрямую связанную с математикой, а именно:
написать функцию, которая выводит все числа от 1 до num без использования циклов.
Помогите другу реализовать такую функцию.
Пример работы программы
> Введите num: 10
> 1
> 2
> 3
> 4
> 5
> 6
> 7
> 8
> 9
> 10
"""


# def write_out_nums(num: int, help_num: int = 1) -> int:
#     if help_num == num:
#         return num
#     print(help_num)
#     help_num += 1
#     return write_out_nums(num, help_num)
#
#
# print(write_out_nums(12))


def print_n(n: int):
    if n == 0:
        return
    print_n(n - 1)
    print(n)

n = int(input())
print_n(n)



