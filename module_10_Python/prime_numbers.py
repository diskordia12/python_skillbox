# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.

# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна итерация — одно число.

# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.

# Количество простых чисел в последовательности: 4.

#

number_amount = int(input('Enter an amount of numbers: '))
prime_number = 0


def is_prime_number(n: int) -> bool:
    from math import sqrt
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(1, number_amount + 1):
    number = int(input(f'Enter {i} number: '))
    if is_prime_number(number):
        prime_number += 1

print(f'Amount of simple numbers: {prime_number}')



