print('Task 5. Vasya')

# Вася вдохновился фильмом «Двадцать одно» и решил изучить математику игровых автоматов.
# Для анализа данных ему нужна информация о том, как часто в автомате выпадает три или две
# одинаковых картинки. Для сбора данных нужна программа, проверяющая это равенство.

# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести один из вариантов:
# 1) 3 (если все совпадают)
# 2) 2 (если два совпадают)
# 3) 0 (если все числа разные)

number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
number_3 = int(input('Enter the third number: '))

# if number_1 == number_2:
#     if number_2 == number_3:
#         print('3')
#     else:
#         print('2')
# elif number_1 == number_3:
#     print('2')
# elif number_2 == number_3:
#     print('2')
# else:
#     print('0')

if number_1 == number_2 and number_1 ==number_3:
    print('3')
elif (number_1 == number_2) or (number_1 ==number_3) or (number_2 == number_3):
    print('2')
else:
    print('0')


