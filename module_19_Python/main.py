"""
Задача 1. Создание кортежей
Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
Также заполните второй кортеж числами от −5 до 0.
Объедините два кортежа, создав тем самым третий кортеж.
С помощью метода кортежа определите в нём количество нулей.
Выведите на экран третий кортеж и количество нулей в нём.
"""
import random
from typing import Dict, Any

# import random
#
#
# first_tuple = tuple([random.randint(0, 5) for _ in range(10)])
# second_tuple = tuple([random.randint(-5, 0) for _ in range(10)])
# print(first_tuple)
# print(second_tuple)
# third_tuple = tuple(first_tuple + second_tuple)
# print(third_tuple)
# print(f'Amount of zeros: {third_tuple.count(0)}')


"""
Задача 2. Цилиндр
Андрей однажды уже писал функции для расчёта площади сферы и объёма шара.
И теперь для своей курсовой работы ему пришлось связаться с цилиндрами.
Пользователь вводит два значения: радиус и высоту.
Напишите функцию для расчёта площади боковой поверхности цилиндра и его полной площади.
Функция должна возвращать два эти значения.
После этого в основной программе выводятся оба ответа в две строки.

Площадь боковой поверхности (r — радиус, h — высота):
side = 2 * pi * r * h
Полная площадь (S — площадь круга, которая вычисляется по формуле pi * r ** 2):
full = side * 2 * S
"""

# from math import pi


# def get_area(r: float, h: float) -> tuple:
#     side = 2 * pi * r * h
#     full = side + 2 * (pi * r ** 2)
#     return side, full
#
#
# radius = float(input('Enter the radius of cylinder: '))
# height = float(input('Enter the height of cylinder: '))
#
# side_area, full_area = get_area(radius, height)
# print(f'The side area: {side_area:.2f}\n'
#       f'The full area: {full_area:.2f}')


"""
Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел.
Затем вызывается функция, которая получает на вход кортеж чисел,
генерирует случайный индекс и случайное значение,
а затем по этим индексу и значению меняет сам кортеж.
Функция должна возвращать кортеж и случайное значение.
В основном коде функция используется два раза, и на экран два раза выводится новый кортеж и
случайное значение. Причём второй раз выводится сумма первого случайного значения и второго.

Однако код, который вам дали, оказался нерабочим. Исправьте его в соответствии с описанием.

import random

def change(nums):
    index = random.randint(0, 5)
    value = random.randint(100, 1000)
    nums[index] = value
    return nums, value

my_nums = 1, 2, 3, 4, 5
new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums = change(new_nums)
rand_val += change(new_nums)
print(new_nums, rand_val)
"""
#
# import random
#
#
# def change(nums):
#     nums = list(nums)
#     index = random.randint(0, 4)
#     value = random.randint(100, 1000)
#     nums[index] = value
#     return tuple(nums), value
#
#
# my_nums = (1, 2, 3, 4, 5)
#
# new_nums, rand_val = change(my_nums)
# print(f'new_nums: {new_nums}, rand_val: {rand_val}')
# print()
#
# new_nums_new, rand_val_new = change(new_nums)
# rand_val += rand_val_new
# print(f'new_nums: {new_nums_new}, rand_val: {rand_val}, rand_val_new: {rand_val_new}')

"""
Задача 1. Саботаж!
Какой-то нехороший человек решил подпортить жизнь frontend-разработчикам и добавил
в код сайта символ ~ (тильда).
Но программисты быстро решили эту проблему, пройдясь по всему коду маленькой программой.
Пользователь вводит строку. Напишите программу, которая проходит по строке и выводит в консоль
индексы символа ~. Для решения этой задачи (и остальных тоже) используйте функцию enumerate.

Пример:
Строка: so~mec~od~e
 
Ответ: 2 6 9 
"""

# user_message = input('Enter your message: ')
# result = list()

# for index, sym in enumerate(user_message):
#     if sym == '~':
#         result.append(index)
#
# print(f'Result: {result}')
#
# # Their way
# def get_indexes(where_to_search, what_to_search):
#     return [str(index) for index, letter in enumerate(where_to_search) if letter == what_to_search]
#
#
# text = input("Введите текст: ")
# print("Ответ:", " ".join(get_indexes(text, "~")))

"""
Задача 2. Словари из списков
Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться).
Затем для каждого списка создайте словарь из пар «индекс — значение» и
выведите оба словаря на экран.

Подсказка: random
Пример: 
Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']

Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}
Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}
"""
#
#
# def create_list() -> list:
#     return [chr(random.randint(ord('a'), ord('z'))) for _ in range(10)]
#
# #
# # def create_dict(letters_seq: list) -> dict:
# #     return {index: letter for index, letter in enumerate(letters_seq)}
#
#
# first_letters_seq = create_list()
# second_letters_seq = create_list()
#
# first_dict = dict(enumerate(first_letters_seq))
# second_dict = dict(enumerate(second_letters_seq))
#
# print(f'First list: {first_letters_seq}')
# print(f'Second list: {second_letters_seq}')
# print(f'First dict: {first_dict}')
# print(f'Second dict: {second_dict}')

"""
Задача 3. Универсальная программа
Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд.
При этом он заранее предупредил, что скрипт должен уметь работать с любым итерируемым типом данных.

Напишите функцию, которая возвращает список из элементов итерируемого объекта
(кортежа, строки, списка, словаря), у которых индекс чётный.

Пример 1:
> Допустим, есть такая строка: 'О Дивный Новый мир!'
> Результат: ['О', 'Д', 'в', 'ы', ' ', 'о', 'ы', ' ', 'и', '!']

> Пример 2:
> Допустим, есть такой список: [100, 200, 300, 'буква', 0, 2, 'а']
> Результат: [100, 300, 0, 'а']

Примечание: для проверки типа можно использовать функцию 
isinstance(<элемент>, <тип данных>), которая возвращает True, если элемент принадлежит
к этому типу данных, и возвращает False в противном случае.
"""

#
# def get_even_elem(data) -> list:
#     result = list()
#     if isinstance(data, dict):
#         data = data.values()
#     for index, value in enumerate(data):
#         if index % 2 == 0:
#             result.append(value)
#     return result
#
#
# print(get_even_elem('О Дивный Новый мир!'))
# print(get_even_elem([100, 200, 300, 'буква', 0, 2, 'а']))
# print(get_even_elem({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))


"""
Задача 1. Кризис миновал
Закупки грейпфрутов прекратились, и кризис в торговой компании закончился.
И теперь можно вернуться к обыденным делам.
Однако внезапно вы обнаружили, что старый скрипт, который выводит данные о фруктах,
куда-то потерялся. Необходимо его восстановить.
Дан словарь с парами «название фрукта — цена»:
incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

Вывести на экран словарь в следующем виде:
apple -- 5600.2
orange -- 3500.45
banana -- 5000.0
bergamot -- 3700.56
durian -- 5987.23
peach -- 10000.5
pear -- 1020.0
persimmon -- 310.0

Не используйте обращение по ключу словаря.
"""
#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# for fruit, price in incomes.items():
#     print(f'{fruit} -- {price}')
#


"""
Задача 2. Сервер
У вас есть данные о сервере, которые хранятся в виде вот такого словаря:

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

 

Напишите программу, которая выводит для пользователя эти данные так же красиво и понятно,
как они представлены в словаре.
Результат работы программы:

server:
    host: 127.0.0.1
    port: 10
configuration:
    access: true
    login: Ivan
    password: qwerty

"""

# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
#
# for main_info, internal_info in server_data.items():
#     print(f'{main_info}: ')
#     for parameter, value in internal_info.items():
#         print(f'\t{parameter}: {value}')
#


"""
Задача 3. В одну строчку
Нашему другу дали задачу: «Есть словарь, в котором ключи — это числа от 0 до 4,
а значения ключей — числа 0, 100, 144, 20 и 19 соответственно.
Нужно написать программу, которая выводит список тех значений,
у которых ключ делится на 2. Причём программа должна быть в одну строчку.»
Программа у друга работает, но её не приняли,
так как в ней не используется правило «не повторяйся» — это когда части кода не повторяются.
Помогите другу исправить решение задачи так, чтобы код в строчке не повторялся. 

Решение друга:
print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if i_key % 2 == 0])
"""

# print([v for k, v in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if k % 2 == 0])

"""
Задача 1. Паспортные данные
В базе данных поликлиники хранятся паспортные данные людей. Хранение реализовано с помощью словаря,
состоящего из пар «Серия и номер паспорта — фамилия и имя».
Серия и номер — составной ключ, а фамилия и имя — составное значение.

data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

Реализуйте функцию, которая по номеру и серии паспорта выдаёт имя и фамилию человека.
"""

#
# def get_name(seria: int, number: int, data: dict) -> tuple:
#     full_name = (seria, number)
#     return data.get(full_name)
#
#
# data = {
#     (5000, 123456): ('Иванов', 'Василий'),
#     (6000, 111111): ('Иванов', 'Петр'),
#     (7000, 222222): ('Медведев', 'Алексей'),
#     (8000, 333333): ('Алексеев', 'Георгий'),
#     (9000, 444444): ('Георгиева', 'Мария')
# }
#
#
# passport_seria = int(input('Enter the passport seria: '))
# passport_number = int(input('Enter the passport number: '))
#
# surname, name = get_name(passport_seria, passport_number, data)
# print(f'Surname: {surname}, name: {name}')
#
#
# # number_and_series = (number, series)
# #
# # if number_and_series in data:
# #     print(data[number_and_series])
# # else:
# #     print("Такого человека нет")


"""
Задача 2. Контакты 2
Мы уже реализовывали телефонную книгу для Степана, однако её проблема была в том,
что туда нельзя было добавить людей с одинаковыми именами. Надо это исправить.

Напишите программу, которая запрашивает у пользователя
имя контакта, фамилию и номер телефона, добавляет их в словарь и выводит на экран
текущий словарь контактов.
Словарь состоит из пар «Ф. И. — телефон», где Ф. И. — это составной ключ.
Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы).
Обеспечьте контроль ввода:
если этот человек уже есть в словаре, то выведите соответствующее сообщение.
"""
telephone_book = dict()

while True:
    name = input('Enter a name: ')
    surname = input('Enter a surname: ')
    full_name = (surname, name)

    if full_name in telephone_book:
        print('You already have a person under this name')
        continue

    phone_number = int(input('Enter a phone number: '))

    telephone_book[full_name] = phone_number
    print(telephone_book)
