"""
В прошлый раз учитель написал программу,
которая выводит числа в формате плавающей точки, однако он вспомнил,
что не учёл одну важную штуку: числа-то могут идти от нуля.

Задано положительное число x (x > 0).
Ваша задача преобразовать его в формат плавающей точки,
то есть x = a * 10 ** b, где 1 ≤ а < 10

Обратите внимание, что x теперь больше нуля, а не больше единицы.
Обеспечьте контроль ввода.

Пример 1:

> Введите число: 92345
> Формат плавающей точки: x = 9.2345 * 10 ** 4

Пример 2:

> Введите число: 0.0012
> Формат плавающей точки: x = 1.2 * 10 ** -3
"""

try:
    x = float(input('Enter a number bigger than 0: '))
    if x <= 0:
        raise ValueError('Negative x')
except ValueError as e:
    print(f'Error: {e}')
    exit(-1)


multiplier = 0.1 if x > 1 else 10
power_counter = 0
mantissa = x
while mantissa > 10 or mantissa < 1:
    mantissa *= multiplier
    power_counter += 1
print(f'Floating point format: x = {round(mantissa, 2)} * 10 ** {power_counter if x > 10 else -power_counter}')

"""
This was my first way
"""
# if 0 < x < 1:
#     count_negative_power = 0
#     while x < 1:
#         x *= 10
#         count_negative_power += 1
#     print(f'Floating point format: x = {round(x, 2)} * 10 ** {-count_negative_power}')
# elif x > 1:
#     count_positive_power = 0
#     while x > 10:
#         x /= 10
#         count_positive_power += 1
#     print(f'Floating point format: x = {round(x, 2)} * 10 ** {count_positive_power}')
# else:
#     print('You should enter only a number bigger that 0')
