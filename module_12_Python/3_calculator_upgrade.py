"""
Степан использует калькулятор для расчёта суммы и разности чисел,
но на работе ему требуются не только обычные арифметические действия.

Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

Напишите программу, запрашивающую у пользователя число и действие,
которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру.

Каждое действие оформите в виде отдельной функции, а основную программу зациклите.
Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.
"""


def summa_n(number: int) -> int:
    summ = 0
    for n in str(number):
        summ += int(n)
    return summ


def max_digit(number: int) -> int:
    max_d = 0
    while number > 0:
        last_digit = number % 10
        max_d = max(max_d, last_digit)
        number //= 10
    # for n in str(number):
    #     if max_d < int(n):
    #         max_d = int(n)
    return max_d


def min_digit(number: int) -> int:
    min_d = number % 10
    while number > 0:
        last_digit = number % 10
        min_d = min(min_d, last_digit)
        number //= 10
    # for n in str(number):
    #     if min_d > int(n):
    #         min_d = int(n)
    return min_d


while True:
    try:
        user_number = int(input('Enter a number: '))
        choice = int(input('What do you want to get:\n'
                           '1 - Sum of numbers\n'
                           '2 - Max digit\n'
                           '3 - Min digit\n'))

        if choice == 1:
            print(f'Sum of numbers from {1} to {user_number} is {summa_n(user_number)}')
        elif choice == 2:
            print(f'Max digit is {max_digit(user_number)}')
        elif choice == 3:
            print(f'Min digit is {min_digit(user_number)}')
        else:
            print('Error. Enter 1 , 2 or 3')

    except ValueError as e:
        print(f'Error: {e}')
