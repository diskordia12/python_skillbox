"""GCD
The greatest common divisor
Напишите функцию, вычисляющую наибольший общий делитель двух чисел
"""


def GCD_recursive(first: int, second: int) -> int:
    """Recursive implementation"""
    if first == 0:
        return second
    if second == 0:
        return first
    return GCD_recursive(max(first, second) % min(first, second), min(first, second))


def get_GCD(first_number: int, second_number: int) -> int:
    # Способ Евклида (Euclid's algo)
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    # We sum first and second, because no matter what one of them 0 and one of them GCD
    return first_number + second_number


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(f'The greatest common divisor (GCD): {get_GCD(a, b)}')
print(f'The greatest common divisor (GCD) recursive: {GCD_recursive(a, b)}')
