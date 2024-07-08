"""
Пользователь вводит два числа — N и K.
Напишите программу, которая заменяет каждое число на число,
которое получается из исходного записью его цифр в обратном порядке,
затем складывает их, снова переворачивает и выводит ответ на экран

Пример:
> Введите первое число: 102
> Введите второе число: 123
> Первое число наоборот: 201
> Второе число наоборот: 321

> Сумма: 522
> Сумма наоборот: 225

"""


def get_reversed(number: int) -> int:

    reversed_number = 0
    while number > 0:
        digit = number % 10
        number //= 10
        reversed_number *= 10
        reversed_number += digit
    return reversed_number


try:
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the second number: '))
except ValueError as e:
    print(f'Error: {e}')
    exit(-1)

reversed_first_number = get_reversed(first_number)
reversed_second_number = get_reversed(second_number)
print(f'The first number is reversed: {reversed_first_number} ')
print(f'The second number is reversed: {reversed_second_number} ')
summ = reversed_first_number + reversed_second_number
print(f'Summ: {summ}')
print(f'Reversed sum: {get_reversed(summ)}')
