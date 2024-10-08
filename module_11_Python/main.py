# Задача 1. Ставки на спорт
# Нас наняла букмекерская контора, где проводятся ставки на конный спорт.
# Напишите программу расчёта потенциального выигрыша игрока.
# Для этого вводится его ставка в рублях и коэффициент (вещественное число),
# а выводится их произведение в качестве потенциального выигрыша.
#
# Пример:
#
# Сколько ставим? 1234
# Какой коэффициент? 1.716
# Потенциальный выигрыш: 2117.544
#
# Усложнение задачи: сделайте так, чтобы после точки выводилось не больше двух цифр.

# bet = float(input('How much do you want to bet: '))
# coefficient = float(input('Enter a coefficient: '))
#
# win = round(bet * coefficient, 2)
# print(f'Your potential profit: {win}')

# Задача 2. День рождения
# В честь дня рождения сына отец не придумал ничего лучше,
# кроме как подарить денег.
# Зато он придумал хоть и странную, но интересную формулу,
# по которой высчитывается сколько он подарит:
# возраст сына умножается на 1.5 и на его температуру тела.
# Остаётся только позавидовать такой фантазии.
#
# Напишите программу, которая запрашивает у пользователя возраст (целое число)
# и температуру тела (вещественное число)
# и в результате выводит сколько отец подарит сыну денег на день рождения.

# age = int(input('Enter your age: '))
# temperature = float(input('Enter a temperature of your body: '))
#
# present = round(1.5 * age * temperature, 2)
# print(f'The present is {present} euros')


# Задача 3. Индекс массы тела
# Алексей работает диетологом в частной клинике,
# каждый день он принимает пациентов разных возрастов
# и с разными показателями роста (в метрах) и веса (в кг).
# Для каждого человека ему нужно считать индекс массы тела
# - это вес поделить на рост в квадрате.
# По государственным стандартам индекс округляется до двух знаков после точки.
# Затем по этому индексу определяется, всё ли в порядке у человека с массой тела:
# если до 18.5, то недобор;
# до 25 - всё нормально,
# до 30 уже идёт избыток,
# а после 30 - ожирение.

# height = float(input('Enter your height: '))
# weight = float(input('Enter your weight: '))
#
# bmi = round(weight / height ** 2, 2)
# print(f'Your bmi is {bmi}')
#
# if bmi <= 18.5:
#     print('You are underweight')
# elif bmi < 25:
#     print('You weight is alright')
# elif bmi < 30:
#     print('You are overweight')
# else:
#     print('You have obesity')


# Задача 1. Космические рейнджеры
# В далеком (а может и не очень) будущем на некоторой планете можно купить космический корабль
# за пол-кредита (CR).
# Один CR это 2200 чатлов.
# Причем чатлы неделимы и являются всегда целым числом.
# Напишите простую программу-конвертор валют.
# В программу вводится количество чатлов,
# а она сообщает сколько это CR и сколько кораблей можно купить на эту сумму.
#
# Пример 1:
#
# Сколько чатлов? 3150
# Это 1.4318181818181819 CR
# Можно купить кораблей: 2
#
# Пример 2:
# Сколько чатлов? 4400
# Это 2.0 CR
# Можно купить кораблей: 4

# chattles = int(input('Enter amount of chattles: '))
# CR = chattles / 2200
# print(f'It is {CR} CR')
# ships = int(CR) * 2
# print(f'You can buy {ships} ships')
#

# Задача 2. Компьютерное зрение
# Вы участвуете в разработке робота, который играет в шахматы на реальной,
# физической шахматной доске размером 0.8 х 0.8 метра.
# Робот смотрит камерой на доску и видит расположение фигур в вещественных числах
# с очень высокой точностью.
#
# Напишите программу, в которую вводятся вещественные координаты шахматной фигуры,
# а программа определяет в какой клетке доски находится эта фигура.
# Каждая клетка доски имеет размер 10х10 см и целочисленные координаты,
# состоящие из двух чисел. Например левая верхняя клетка имеет целые координаты (0, 0),
# справа от неё клетка (1, 0) а снизу (0, 1).
# Также обеспечьте контроль ввода: нельзя выходить за границы доски.
#
# Пример:
#
# Введите местоположение фигуры
# По горизонтали: 0.731
# По вертикали: 0.149
#
# Фигура находится в клетке (7, 1)
#
# Введите местоположение фигуры
# По горизонтали: 0.833
# По вертикали: -0.132
#
# Клетки с такой координатой не существует

# x = float(input(' Enter coordinate of x: '))
# y = float(input(' Enter coordinate of y: '))
#
# if 0 <= x <= 0.8 and 0 <= y <= 0.8:
#     x_square = int(x * 10)
#     y_square = int(y * 10)
#     print(f'Figure on the ({x_square},{y_square}) cell')
# else:
#     print('There is no cell with this coordinates')

# Задача 3. Точность и аккуратность
# Робот из задачи “Компьютерное зрение” правильно определяет на какой клетке стоят фигуры.
# Но вот беда, часто по вине соперника-человека фигуры стоят на доске
# не ровно по центру клетки, а со смещением.
# Если во время игры такое смещение станет слишком велико,
# то станет непонятно в какой клетке стояла фигура.
# Чтобы избежать этой ситуации нужно чтобы робот поправлял фигуры на доске,
# выставляя их по центру клетки. Модифицируйте программу “Компьютерное зрение” так,
# чтобы она выдавала не только номера клетки,
# в которой находится фигура но и две вещественных поправки:
# на сколько нужно подвинуть фигуру по горизонтали и вертикали для того чтобы
# она оказалась по центру своей клетки.
#
# Пример:
#
# Введите местоположение фигуры
# По горизонтали: 0.731
# По вертикали: 0.167
# Фигура находится в клетке (7, 1)
# Поправьте положение фигуры на (0.019, -0.017)

# x = float(input(' Enter coordinate of x: '))
# y = float(input(' Enter coordinate of y: '))
#
# if 0 <= x <= 0.8 and 0 <= y <= 0.8:
#     x_square = int(x * 10)
#     y_square = int(y * 10)
#     adjust_x = round((x_square + 0.5) / 10 - x, 3)
#     adjust_y = round((y_square + 0.5) / 10 - y, 3)
#     print(f'Figure on the ({x_square},{y_square}) cell\n'
#           f'Adjust figure position on ({adjust_x},{adjust_y})')
#
# else:
#     print('There is no cell with this coordinates')


# Задача 1. Герон
# Существует, так называемая, формула Герона,
# позволяющая вычислить площадь треугольника, зная длины его сторон.
#
# S= √ (p * (p - a)*(p - b)*(p - c)) ,где
#
# S - площадь;
# p - полупериметр треугольника (a+b+c)/2;
# a,b,c - длины сторон треугольника.
#
# Напишите программу, которая принимает на вход длины сторон треугольника и выводит его площадь
import math

# a = float(input('Enter length of a: '))
# b = float(input('Enter length of b: '))
# c = float(input('Enter length of c: '))
#
# p = (a + b + c) / 2
# S = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print(f'Triangles area is {S}')


# Задача 2. Игра
# Вам предстоит создать 2D-игру (вид сверху, игрок двигается в двух плоскостях).
#
# Начнём с управления персонажем: получаем от игрока пройденное расстояние и угол,
# по которому двигался персонаж.
# Зная эту информацию, нужно изменить текущие координаты (0, 0) на новые (х, у).
# Чтобы это сделать, требуется узнать, какое расстояние персонаж преодолеет
# по горизонтали (по оси Х, x = расстояние × косинус угла)
# и по вертикали (по оси У, y = расстояние × синус угла).
#
# Напишите программу, которая получает на вход расстояние и угол поворота.
# Выведите координаты нового местоположения персонажа.

# distance = float(input('Enter your distance: '))
# angle = math.radians(float(input("Enter angle: ")))
#
# x = math.cos(angle) * distance
# y = math.sin(angle) * distance
# print(f'Your coordinates ({x},{y})')

# Задача 3. Мега-калькулятор
# # Кеша учится в третьем классе, и уже умеет программировать на питоне.
# Как и многие его одноклассники, он очень любит сразу применять все полученные знания на практике.
#
# Напишите программу, которая получает от пользователя вещественное число,
# по очереди применяет к нему функции модуля Math и выводит результат:
#
# округляет вниз
# округляет вверх
# берет модуль числа
# извлекает квадратный корень
# возводит экспоненту в степень, равную числу
# считает натуральный логарифм числа
# считает логарифм числа по основанию 2
# считает логарифм числа по основанию 10
# считает синус и косинус числа
# И так как Кеша самый умный в классе, он решил попробовать посчитать факториал числа.
# Для этого ему пришлось придумать и реализовать контроль ввода:
# факториал вычисляется, только если введенное число было натуральным.

n = float(input("Enter a number: "))
print(f' rounded down: {math.floor(n)}')
print(f' rounded up: {math.ceil(n)}')
print(f' abs: {abs(n)}')
print(f' sqrt: {math.sqrt(n)}')
print(f' rexp: {math.exp(n)}')
print(f' ln: {math.log(n, math.e)}')
print(f' log2: {math.log2(n)}')
print(f' log10: {math.log10(n)}')
print(f' sin: {math.sin(math.radians(n))}')
print(f' cos {math.cos(math.radians(n))}')

if n > 0 and n == int(n):
    print(f'factorial: {math.factorial(n)}')
