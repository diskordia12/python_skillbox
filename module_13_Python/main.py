"""Задача 1. Сумма чисел 2
Пользователь вводит число N. Напишите функцию summa_n,
 которая принимает одно целое положительное число N и
  находит сумму всех чисел от 1 до N включительно.
   Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.

Пример работы программы:
> Введите число: 5
> Сумма от 1 до 5 = 15
> Сумма от 1 до 15 = 120
"""
# print('\nTask 1. Sum\n')


# def summa_n(number: int) -> int:
#     summ = 0
#     for n in range(1, number + 1):
#         summ += n
#     return summ
#
#
# user_number = int(input('Enter a number: '))
# summ_numbers = summa_n(user_number)
# print(f'Sum from 1 to {user_number} is {summ_numbers}')
# print(f'Sum from 1 to {summ_numbers} is {summa_n(summ_numbers)}')

"""
Задача 2. «Назад в будущее»
Вы — один из разработчиков языка программирования Python, и вы пишете специальный математический модуль, который можно было бы просто подключить внутри программы и облегчить жизнь всем программистам.

Реализуйте функцию gcd, которая получает два параметра — два числа — и возвращает наибольший общий делитель этих двух чисел.

Пример работы программы:

> Введите первое число: 6
> Введите второе число: 10
> НОД = 2
"""

# print('\nTask 2. GCD\n')


# def get_gcd(first_number: int, second_number: int) -> int:
#     # Способ Евклида (Euclid's algo)
#     while first_number != 0 and second_number != 0:
#         if first_number > second_number:
#             first_number %= second_number
#         else:
#             second_number %= first_number
    # We sum first and second, because no matter what one of them 0 and one of them GCD
#     return first_number + second_number
#
#
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# print(f'The greatest common divisor (GCD): {get_gcd(a, b)}')
#

"""
Another way
"""
#
# def gcd(x, y):
#     if x > y:
#         small = y
#     else:
#         small = x
#     gcd_find = 1
#     for i in range(1, small + 1):
#         if (x % i == 0) and (y % i == 0):
#             gcd_find = i
#
#     return gcd_find
#
#
# first_number = int(input("Первое число: "))
# second_number = int(input("Второе число: "))
# print("НОД=", gcd(first_number, second_number))

"""
Задача 3. Приоритет задач
В одном дата-центре ресурсы распределены так, 
что сначала обрабатываются крупные задачи, а затем уже идут небольшие.
 Каждая из этих задач, по сути, просто огромный поток цифр.
  Ваша задача, как программиста этого центра, написать программу, 
  которая поможет определять, какую из задач нужно решать в первую очередь. 

Вводится последовательность из N чисел. 
Нужно определить номер числа, у которого больше всего цифр, 
и вывести на экран соответствующее сообщение. Если число отрицательное, то считать его за 0. 
Для подсчёта количества цифр реализуйте функцию numeral_count.

Пример работы программы:

> Введите кол-во задач: 4
> Введите число: 6
> Введите число: 14
> Введите число: 1
> Введите число: 13434

> Первая задача на обработку: 13434
"""

# print('\nTask 3. Priority\n')
#
#
# def numeral_count(number: int) -> int:
#     counter = 0
#     while number > 0:
#         counter += 1
#         number //= 10
#     return counter
#

# task_amount = int(input('Enter amount of tasks: '))
# max_number = 0
# priority_task = 0
#
# for i in range(task_amount + 1):
#     number = int(input('Enter a number: '))
#     if number < 0:
#         number = 0

#     digits = numeral_count(number)
#     if max_number < digits:
#         max_number = digits
#         priority_task = number
#
# print(f'The first priority task: {priority_task}')

"""
Задача 1. Возможности компьютера
В одной IT-компании тестируют возможности различных языков программирования,
 компиляторов и, конечно же, компьютеров.
  Компания дала вам задачу понять, какое самое маленькое возможное число можно получить
путём постоянного деления числа на 2. Изначально число равно единице. Также,
помимо самого числа, компания просит вывести количество делений. Реализуйте такую программу.
"""

# print('\nTask 1. Possibilities\n')
#
# number = 1
# small_number = number
# counter = 0
#
# while number != 0:
#     small_number = number
#     number /= 2
#     counter += 1
#
# print(f'Small number: {small_number}\n'
#       f'iterations: {counter - 1}')


"""
Задача 2. Тестирование
Команде программистов отдали на тестирование новую модель суперкомпьютера.
 Для начала программисты решили проверить, как у компьютера обстоят дела
  с вычислениями вещественных чисел. Разработчики компьютера предупредили,
   что на входе он работает только с экспоненциальной формой числа.

Пользователь вводит число N в экспоненциальной форме,
 где мантисса всегда равна числу от 1 до 9, а порядок меньше нуля.
  Также есть переменная Х, которая изначально равна единице.
   Посчитайте, сколько раз нужно прибавить N к Х, чтобы оно перевалило за двойку.

Дополнительно: обеспечьте контроль ввода.

Пример 1:

Введите число в эксп. форме: 1e-3
Кол-во прибавлений: 1001
Пример 2:

Введите число в эксп. форме: 5.02e-1
Кол-во прибавлений: 2
"""
# При желании мы можем усложить контроль ввода и добавить проверки мантиссы и порядка:

# while True:
#     # Если мы хотим проверить мантиссу - то нам нужно работать с числом как со строкой, поэтому float к input добавлять пока не будем
#     delta = input("Введите число в эксп. форме ")
#     # проверка, что мантисса равна числу от 1 до 9
#     # сперва получим отдельно часть строки до символа 'e'
#     mantissa = ''
#     for cipher in delta:
#         if cipher == 'e':
#             break
#         mantissa += cipher
#     # получив мантиссу - мы можем проверить, что она удовлетворяет условию (равна числу от 1 до 9)
#     # так же мы сразу можем добавить проверку порядка - если порядок отрицательный, то введенное число будет меньше 1, это мы и проверим:
#     if 1 <= float(mantissa) <= 9 and float(delta) < 1:
#         print('Число введено верно!')
#         delta = float(delta)
#         break
#     else:
#         print("Число введено с ошибкой, мантисса всегда должна быть равна числу от 1 до 9, а порядок должен быть меньше нуля")


# user_number = float(input('Enter an exponential form of a number: '))
# x = 1
#
# count_add = 0
#
#
# while x < 2:
#     x += user_number
#     count_add += 1
#
#
# print(f'Amount of additions: {count_add}')


"""
Задача 3. Урок информатики
На одном из уроков информатики учитель объяснял тему «Числа с плавающей точкой»,
 но несколько учеников никак не могли понять, почему эта точка «плавает» и как вообще выглядят числа в такой форме. Для наглядности учитель написал программу, которая берёт число больше десяти и выводит его в формате плавающей точки.

Пользователь вводит положительное число x (x > 10). 
Напишите функцию, которая выводит его в формате плавающей точки,
 то есть x=a *10 ** b, где 1≤a<10.

Пример 1:

Введите число: 16
Формат плавающей точки: x = 1.6 * 10 ** 1
Пример 2:

Введите число: 92345
Формат плавающей точки: x = 9.2345 * 10 ** 4
"""

# x = int(input('Enter a number bigger than 10: '))
# a = x / 10 **(len(str(x)) - 1)
# b = (len(str(x)) - 1)
# print(f'Floating point format: {x} = {a} * 10 ** {b}')

"""
Another way
"""

# start_number = float(input("Введите число: "))
# count = 0
# while start_number > 10:
#     count += 1
#     start_number /= 10
#
# print(f"Формат плавающей точки: x = {start_number} * 10 ** {count}")

"""
Задача 1. Опять налоги
У правительства одной из стран есть бухгалтерская программа,
 которая суммирует налоги её граждан, компаний плюс НДС с товаров.
Страна развивалась, суммарные налоги увеличивались, и бухгалтеры заметили,
 что после добавления к общей сумме налогов некого НДС 
 от какого-то продукта общая сумма перестала меняться… 

Нужно помочь бухгалтерам: напишите функцию, на вход которой подаются два числа
 — общая сумма налога tax и новый налог new_tax, который нужно добавить к общей сумме.
  Функция должна проверять, изменится ли показатель степени e при сложении двух чисел.

Пример 1:

Введите бюджет страны: 1.2e-12
Новые поступления (налог): 1.2e1
Результат: Бюджет увеличится
Пример 2:

Введите бюджет страны: 1.23e12
Новые поступления (налог): 1.2e1
Результат: Бюджет не изменится
"""


# def tax_compare(tax: float, new_tax: float):
#     if tax + new_tax != tax:
#         print('Budget wil increase')
#     else:
#         print('Budget won\'t change')
#
#
# country_budget = float(input('Enter a budget: '))
# budget_receipts = float(input('Enter a new tax: '))
# tax_compare(country_budget, budget_receipts)
# print(country_budget + budget_receipts)
# print(country_budget)

# import math
#
#
# def check_exponent_change(tax, new_tax):
#     total = tax + new_tax
#     degree_e_tax = math.floor(math.log10(tax))
#     degree_e_total = math.floor(math.log10(total))
#     if degree_e_tax != degree_e_total:
#         return True
#     else:
#         return False
#
#
# country_budget = float(input('Введите бюджет страны: '))
# budget_receipts = float(input('Введите новые поступления (налог): '))
# is_increase = check_exponent_change(country_budget, budget_receipts)
#
# if is_increase:
#     print('Бюджет увеличится')
# else:
#     print('Бюджет не изменится')

"""
Задача 2. Сравнение
Так как в Python операции с вещественными числами могут давать
 неожиданные результаты (в частности, 0.1 + 0.2 не будет в точности равняться 0.3),
  стоит задача с этим как-то справляться. 

Напишите функцию eqv, которая принимает три числа и затем сравнивает сумму первых двух чисел 
с третьим с определённой степенью точности: до 15-го знака после точки.
 Если равенство выполняется, то функция возвращает True, иначе возвращает False.

Пример 1:

Введите первое число: 1.1
Введите второе число: 2.2
Введите третье число: 3.3
True

Пример 2:

Введите первое число: 1e-14
Введите второе число: 1e-14
Введите третье число: 3e-14
False
"""


def eqv(a: float, b: float, c: float) -> bool:
    summ = a + b
    return abs(summ - c) <= 1e-15


a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
c = float(input('Enter third number: '))
print(eqv(a, b, c))
