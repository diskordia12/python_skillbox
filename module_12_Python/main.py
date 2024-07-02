# Задача 1. Робот
# В одном отеле для эксперимента на вход хотят поставить робота,
# который будет спрашивать у прохожих, не желают ли они зайти.
# При ответе «Да» робот должен приветствовать человека и пустить в отель.
# Для робота написали вот такую программу с использованием функции:

# def greeting():
#     print('Hello!')
#     print('Welcome!')
#
# while True:
#     user_choice = input('Come in? Yes/No: ')
#     if user_choice == 'Yes':
#         greeting()
#     print('\nNext please.\n')


# Задача 2. Провизия
# Одна государственная компания поставляет еду на разные труднодоступные базы
# (полярные, горные и так далее) в разных уголках страны.
# В компании для удобства расчёта количества еды была реализована такая программа:

# def count_food():
#     a = int(input('Amount of food_1: '))
#     b = int(input('Amount of food_2: '))
#     print(f'Total: {a + b} items')
#
#
# print("Сколько мешков рыбы и мяса?")
# count_food()
#
# print("\nСколько буханок белого и чёрного хлеба?")
# count_food()
#
# print("\nСколько вёдер воды и молока?")
# count_food()
#
#Задача 3. Почта
# Василий пришёл получать посылку на почту.
# Разумеется, в почтовом извещении ему нужно было написать свои фамилию, имя и адрес проживания,
# чтобы кто-нибудь не получил посылку за него, например члены его семьи (а им бы хотелось!).

# Напишите функцию для вывода фамилии, имени и адреса для конкретного члена семьи.
# Выведите информацию о нём три раза (без цикла).

# def get_user_info(surname: str, name: str, street: str, house: str):
#     print(f'Surname: {surname}\n'
#       f'Name: {name}\n'
#       f'Street: {street}\n'
#       f'Number of house: {house}\n')
#
# surname = input('Enter your surname: ')
# name = input('Enter your name: ')
# street = input('Enter your street: ')
# house = input('Enter your number of house: ')
#
# get_user_info(surname, name, street, house)
# get_user_info(surname, name, street, house)
# get_user_info(surname, name, street, house)

# Задача 1.
# Одна бутылка воды «КлирВотер» от производителя «ВодЗавод» в разных
# магазинах стоит по - разному.
# Напишите программу, которая три раза вызывает функцию about_water, передаёт
# в неё один аргумент — цену на воду и выводит на # экран# название# воды, производителя
# # и # цену.
#
# Пример:
# # Название: КлирВотер
# # Производитель: ВодЗавод
# Цена: 25

# # Название: КлирВотер
# # Производитель: ВодЗавод
# # Цена: 30
#
# Название: КлирВотер
# Производитель: ВодЗавод
# # Цена: 40


# def about_water(price: int):
#     print(f'Name: Klitwater\n'
#           f'Producer: WaterUsine\n'
#           f'price: {price}')
#
# for _ in range(3):
#     price = int(input('\nEnter price of water: '))
#     about_water(price)


# Задача 2. Вот это объёмы 2
# Андрей продолжает писать курсовую работу по физике,
# и теперь ему нужно находить не только объём планеты, но и её площадь.
# Для этого он использует две такие формулы:
# Формула для площади сферы:
#
# S = 4 * pi * R ** 2
# Формула для объёма шара:
#
# V = 4/3 * pi * R ** 3
#
# Так как в самом курсовом проекте эти формулы пригодятся ещё не раз,
# Андрей решил поступить рационально и просто написать функцию для каждой формулы.
# Напишите программу, которая на вход получает от пользователя радиус планеты (вещественное число)
# и вызывает функции sphere_area и sphereVolume.
# Реализуйте эти функции: первая считает и выводит на экран площадь сферы, вторая — объём шара.

# from math import *
#
# def sphere_area(r: float) -> float:
#     return 4 * pi * r ** 2
#
# def sphere_volume(r: float) -> float:
#     return 4/3 * pi * r ** 3
#
# while True:
#     r = float(input('Enter radius of a planet: '))
#     print(f'Area of a planet: {sphere_area(r)}')
#     print(f'Volume of a planet: {sphere_volume(r)}')


# Задача 3. Простые числа
# Пользователь вводит число N — количество чисел в последовательности. Напишите функцию  is_prime,
# которая проверяет, является ли число простым и выводит ответ в консоль.

# number_amount = int(input('Enter amount of numbers: '))
#
#
# def is_prime(number: int) -> str:
#     from math import sqrt
#     for i in range(2, int(sqrt(number)) + 1):
#         if number % i == 0:
#             return 'is NOT prime'
#     return 'is prime'
#
#
# for i in range(number_amount):
#     number = int(input('Enter a number: '))
#     print(f'Number {is_prime(number)}')


# Задача 1. Среднее арифметическое
# Программа получает от пользователя два числа — a и b.
# Реализуйте функцию, которая принимает на вход числа a и b, считает и выводит
# в консоль среднее арифметическое всех чисел из отрезка [a; b].
# Обеспечьте контроль ввода: не забывайте, что а всегда должно быть меньше, чем b.

# Пример:
# Введите левую границу: 3
# Введите правую границу: 8
# Среднее: 5.5
#
# Усложнение: сделайте это без использования циклов

# import math
#
# def middle(a: int, b: int) -> float:
#     summ = 0
#     for i in range(a, b + 1):
#         summ += i
#     return summ / (b - a + 1)

# left_board = int(input('Enter left board: '))
# right_board = int(input('Enter right board: '))
#
# if left_board > right_board:
#     left_board, right_board = right_board, left_board
#
# print(f'middle: {middle(left_board, right_board)}')
#
# # Without circle
# print(f'middle: {(left_board + right_board) / 2}')

# Задача 2. Почта 2
# На почте немного поменялись правила:
# теперь в почтовом извещении нужно указывать
# фамилию, имя, страну проживания, город, улицу, номер дома и номер квартиры.

# Реализуйте функцию, которая получает все эти данные и выводит на экран.
# В программе вызовите функцию три раза с разными значениями аргументов.

# Подсказка: семь аргументов

# def print_info(surname: str, name: str, country: str, city: str, street: str, house: str, flat: str):
#     print(f'Surname: {surname}\n'
#           f'Name: {name}\n'
#           f'Country: {country}\n'
#           f'City: {city}\n'
#           f'Street: {street}\n'
#           f'House: {house}\n'
#           f'Flat: {flat}\n')
#
# for _ in range(3):
#     user_surname = input("Введите фамилию: ")
#     user_name = input("Введите имя: ")
#     user_country = input("Введите страну проживания: ")
#     user_city = input("Введите город: ")
#     user_street = input("Введите улицу: ")
#     user_house = input("Введите номер дома: ")
#     user_flat = input("Введите номер квартиры: ")
#
#     print_info(user_surname, user_name, user_country, user_city, user_street, user_house, user_flat)


# Задача 3. GPS-навигатор 2.0
# Нам поручили усовершенствовать GPS-навигатор, добавив в него новую фишку.
# Теперь пользователь может не только смотреть расстояние от себя до объекта,
# но и задавать в навигаторе две произвольные точки, после чего на экран ему
# выводится расстояние между ними.
# Для этого пользователь вводит четыре действительных числа x1, y1, x2, y2 —
# это как раз координаты этих двух точек.
#
# Напишите программу, где у пользователя спрашивается,
# чего он хочет — найти расстояние от себя до точки или
# найти расстояние между двумя произвольными точками, после чего
# запрашиваются необходимые координаты точек и выводится ответ на экран

from math import *

def get_distance(x_2: float, y_2: float, x_1: float = 0, y_1: float = 0) -> float:
    return sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

choice = int(input('1 - distance between you and a point\n'
                   '2 - distance between two points\n'
                   ' '))
if choice == 1:
    x_2 = int(input('Coordinate x_2: '))
    y_2 = int(input('Coordinate y_2: '))
    print(f'distance between you and point {x_2, y_2} is {get_distance(x_2, y_2)}')
elif choice == 2:
    x_1 = int(input('Coordinate x_1: '))
    y_1 = int(input('Coordinate y_1: '))
    x_2 = int(input('Coordinate x_2: '))
    y_2 = int(input('Coordinate y_2: '))
    print(f'distance between point {x_1, y_1} and point {x_2, y_2} is {get_distance(x_2, y_2, x_1, y_1)}')
else:
    print('Error of input')
