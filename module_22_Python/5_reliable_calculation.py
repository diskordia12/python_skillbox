"""
Задача 5. Надёжные вычисления
Контекст
Вы работаете в компании, занимающейся финансовыми вычислениями.
Вам необходимо разработать функцию для вычисления квадратного корня числа,
которая будет использоваться в анализе финансовых данных и расчёте инвестиционных показателей.
Вы понимаете, что передача отрицательного числа или возникновение других ошибок вычисления могут
привести к непредсказуемым результатам.

Задача
Напишите функцию, которая будет:
- Вычислять и возвращать квадратный корень полученного числа.
- Обрабатывать исключения для отрицательных чисел и других возможных ошибок.

Советы
При помощи оператора as вы можете сохранить пойманную ошибку в переменную,
чтобы затем использовать её для получения дополнительной информации:

except Exception as exc:
    print(exc)
Старайтесь не смешивать конкретные исключения, которые вы ожидаете,
со всеми другими (except Exception будет ловить все исключения,
которые не были пойманы предыдущими except).
"""

from math import sqrt


def get_sqrt(number: int):
    try:
        return sqrt(number)
    except ValueError:
        print('Digit must be positive')
    except TypeError:
        print('Must be digit not string')



print(get_sqrt(16), '\n')
print(get_sqrt(-4), '\n')
print(get_sqrt('4'), '\n')


user_number = float(input('Enter a number: '))
result = get_sqrt(user_number)

if result is None:
    print('Error in calculating the sqrt')
else:
    print(f'Sqrt from {user_number} is {result}')

