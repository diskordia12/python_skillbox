"""
Задача 1. Квадраты чисел
Пользователь вводит число N.
Напишите программу, которая генерирует последовательность
из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее).
Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.
"""


# With class-iterator
class Squares:

    def __init__(self, end: int):
        self.end = end
        self.count = 0

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.end:
            raise StopIteration
        return self.count ** 2


print('With class-iterator')
number_amount = int(input('\nEnter a number: '))
user_squares = Squares(number_amount)
for num in user_squares:
    print(num, end='\t')


# With function generator
def get_squares(n: int) -> int:
    for num in range(1, n + 1):
        yield num ** 2


print('\nWith function generator')
user_squares_2 = get_squares(number_amount)
for num in user_squares_2:
    print(num, end='\t')


# With generator expression
number_amount = int(input('\nEnter a number: '))
user_squares_3 = (number ** 2 for number in range(1, number_amount + 1))
print('\nWith generator expression')
for number in user_squares_3:
    print(number, end='\t')
