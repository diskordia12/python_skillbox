"""Sum of digits
Напишите функцию summa_n,
которая принимает одно целое положительное число N
и выводит сумму всех чисел от 1 до N включительно.

Пример работы программы:
> Введите число: 5
> Я знаю, что сумма чисел от 1 до 5 равна 15
"""


def summa_n(number: int) -> int:
    # Using arithmetic progression n * (n+1) / 2
    # return number * (number + 1) / 2
    summ = 0
    for n in range(1, number + 1):
        summ += n
    return summ


user_number = int(input('Enter a number: '))
print(f'I know, that sum of numbers from {1} to {user_number} is {summa_n(user_number)}')
