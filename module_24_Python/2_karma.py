"""
Задача 2. Карма
Один буддист-программист решил создать свой симулятор жизни,
в котором нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы
от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:
- KillError,
- DrunkError,
- CarCrashError,
- GluttonyError,
- DepressionError.
(Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
Напишите такую программу.
Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении кармы
до уровня константы.
Исключения обработайте и запишите в отдельный лог karma.log.

По итогу у вас может быть примерно такая структура программы:
открываем файл
цикл по набору кармы
   try
      карма += one_day()
   except(ы) с указанием классов исключений, которые нужно поймать
      добавляем запись в файл
закрываем файл
"""
import random

MAX_CARMA = 500


class KillError(Exception):
    def __str__(self):
        return 'Kill Error'


class DrunkError(Exception):
    def __str__(self):
        return 'Drunk Error'


class CarCrashError(Exception):
    def __str__(self):
        return 'Car crash Error'


class GluttonyError(Exception):
    def __str__(self):
        return 'Gluttony Error'


class DepressionError(Exception):
    def __str__(self):
        return 'Depression Error'


def one_day():
    karma_strike_flip = random.randint(1, 10)
    if karma_strike_flip == 5:
        # day_exception = random.randint(0, 4)
        day_exception = random.choice((KillError, DrunkError, CarCrashError, GluttonyError, DepressionError))
        raise day_exception

    return random.randint(1, 7)


person_karma = 0
day = 0
with open('karma.log', 'w') as file:
    while person_karma < MAX_CARMA:
        day += 1
        try:
            person_karma += one_day()
        except Exception as e:
            file.write(str(day) + ' day: ' + str(e) + '\n')

