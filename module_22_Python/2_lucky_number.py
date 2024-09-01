"""
Задача 2. Счастливое число
Напишите программу, которая запрашивает у пользователя число до тех пор,
пока сумма запрашиваемых чисел не станет больше либо равна 777.
Каждое введённое число при этом дозаписывается в файл out_file.txt.
Сделайте так, чтобы перед дозаписью программа с вероятностью 1 к 13
выдавала пользователю случайное исключение и завершалась.

Пример 1
> Введите число: 10
> Введите число: 500
> Введите число: 200
> Введите число: 67
> Вы успешно выполнили условие для выхода из порочного цикла!

Содержимое файла out_file.txt:
> 10
> 500
> 200
> 67

Пример 2
> Введите число: 10
> Введите число: 500
> Вас постигла неудача!

Содержимое файла out_file.txt:
> 10
"""

import random

user_sum_number = 0

try:
    while user_sum_number < 777:
        user_number = int(input('Enter a number: '))
        user_sum_number += user_number
        break_number = random.randint(0, 13)
        if break_number == 13:
            raise RuntimeError('You have failed! Just like that...')
        with open('out_file.txt', 'a') as out_file:
            out_file.write(str(user_number) + '\n')
            # out_file.write('\n')
except RuntimeError as e:
    print(e)
else:
    print('You have successfully fulfilled the condition for breaking the vicious cycle!')


print('Contents of the file out_file.txt')
with open('out_file.txt', 'r') as final_file:
    for line in final_file:
        print(line, end='')

