"""
Вводится последовательность чисел, которая оканчивается нулём.

Реализуйте функцию, которая принимает в качестве аргумента каждое число,
переворачивает его и выводит на экран.

Пример:
> Введите число: 1234
> Число наоборот: 4321

> Введите число: 1000
> Число наоборот: 0001

> Введите число: 0
> Программа завершена!

Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.

> Введите число: 1230
> Число наоборот: 321

Кстати, нули, которые мы убрали, называются ведущими.
"""


def get_reversed(number: int) -> int:

    reversed_number = 0
    while number > 0:
        digit = number % 10
        number //= 10
        reversed_number *= 10
        reversed_number += digit
    return reversed_number


while True:
    try:
        user_number = int(input('Enter a number: '))

        if user_number == 0:
            print('The program is completed!')
            break

        print(f'Reversed number: {get_reversed(user_number)}')
    except ValueError as e:
        print(f'Error: {e}')
