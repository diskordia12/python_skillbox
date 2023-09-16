print('Task 8. Maximum number')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
third_number = float(input('Enter the third number: '))

if first_number > second_number: # Определяю первое или второе число больше
    maximum = first_number  # записываю в новую переменную максимальное из двух
else:
    maximum = second_number

if third_number > maximum:
    maximum = third_number

print(f'maximum {maximum}')




