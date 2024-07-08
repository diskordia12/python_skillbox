"""
Юра пишет различные полезные функции для Python,
чтобы остальным программистам стало проще работать.
Он захотел написать функцию, которая будет находить максимум из перечисленных чисел.
Функция для нахождения максимума из двух чисел у него уже есть.
Юра задумался: может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?

Помогите Юре написать программу, которая находит максимум из трёх чисел.
Для этого используйте только функцию нахождения максимума из двух чисел.

По итогу в программе должны быть реализованы две функции:
1) maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
2) maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх);
при этом она должна использовать для сравнений первую функцию maximum_of_two.

"""


def maximum_of_two(number_1: float, number_2: float) -> float:
    return number_1 if number_1 > number_2 else number_2


def maximum_of_three(number_1: float, number_2: float, number_3: float) -> float:
    return maximum_of_two(number_1, maximum_of_two(number_2, number_3))
    # max_of_two = maximum_of_two(number_2, number_3)
    # return number_1 if number_1 > max_of_two else max_of_two


first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
third_number = float(input('Enter the third number: '))

print(f'Max: {maximum_of_three(first_number, second_number, third_number)}')
