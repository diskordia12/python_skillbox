"""
Задача 1. Машина
Напишите класс Toyota, состоящий из четырёх статических атрибутов:
- цвет машины (например, красный),
- цена (один миллион),
- максимальная скорость (200),
- текущая скорость (ноль).
Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости
на случайное число от нуля до 200.
"""
#
# import random
#
# class Toyota():
#     car_color = 'red'
#     car_price = 1e6
#     car_max_speed = 200
#     current_speed = 0
#
#
# car_1 = Toyota()
# car_2 = Toyota()
# car_3 = Toyota()
#
# car_1.current_speed = random.randint(0, 200)
# car_2.current_speed = random.randint(0, 200)
# car_3.current_speed = random.randint(0, 200)
#
#
# print(car_1.current_speed)
# print(car_2.current_speed)
# print(car_3.current_speed)


"""
Задача 2. Однотипные объекты
В офис заказали небольшую партию из четырёх мониторов и трёх наушников.
У монитора есть четыре характеристики:
- название производителя
- матрица
- разрешение
- частота обновления экрана.
Все четыре монитора отличаются только частотой.

У наушников три характеристики:
- название производителя
- чувствительность
- наличие микрофона.
Отличие только в наличии микрофона.

Для внесения в базу программист начал писать такой код:
monitor_name_1 = 'Samsung'
monitor_matrix_1 = 'VA'
monitor_res_1 = 'WQHD'
monitor_freq_1 = 60

monitor_name_2 = 'Samsung'
monitor_matrix_2 = 'VA'
monitor_res_2 = 'WQHD'
monitor_freq_2 = 144

monitor_name_3 = 'Samsung'
monitor_matrix_3 = 'VA'
monitor_res_3 = 'WQHD'
monitor_freq_3 = 70

monitor_name_4 = 'Samsung'
monitor_matrix_4 = 'VA'
monitor_res_4 = 'WQHD'
monitor_freq_4 = 60

headphones_name_1 = 'Sony'
headphones_sensitivity_1 = 108
headphones_micro_1 = False

headphones_name_2 = 'Sony'
headphones_sensitivity_2 = 108
headphones_micro_2 = True

headphones_name_3 = 'Sony'
headphones_sensitivity_3 = 108
headphones_micro_3 = True

Поправьте программиста: перепишите код, используя классы и экземпляры классов.
"""

#
# class Monitor():
#     monitor_name = 'Samsung'
#     monitor_matrix = 'VA'
#     monitor_res = 'WQHD'
#     monitor_freq = 60
#
#
# class Headphones():
#     headphones_name = 'Sony'
#     headphones_sensitivity = 108
#     headphones_micro = True
#
#
# # monitor_1 = Monitor()
# # monitor_2 = Monitor()
# # monitor_3 = Monitor()
# # monitor_4 = Monitor()

# monitors = [Monitor() for _ in range(4)]
# headphones = [Headphones() for _ in range(3)]
#
# for index, number in enumerate([60, 144, 70, 60]):
#     monitors[index].monitor_freq = number
#
# headphones[0].headphones_micro = False

"""
Задача 1. Машина 2
Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
- цвет машины (например, красный),
- цена (один миллион),
- максимальная скорость (200),
- текущая скорость (ноль).

Добавьте два метода класса:
- Отображение информации об объекте класса.
- Метод, который позволяет устанавливать текущую скорость машины.
Проверьте работу этих методов.
"""

#
# class Toyota:
#     car_color = 'red'
#     car_price = 1e6
#     car_max_speed = 200
#     current_speed = 0
#
#     def info(self):
#         print(f'car color: {self.car_color}\n'
#               f'car price: {self.car_price}\n'
#               f'car max speed: {self.car_max_speed}\n'
#               f'current speed: {self.current_speed}\n')
#
#     def set_current_speed(self, speed):
#         self.current_speed = speed
#
#
# my_car = Toyota()
# my_car.info()
# my_car.set_current_speed(36)
# my_car.info()
#
# # обратите внимание, что скорость внутри Класса осталась той же, её изменения не коснулись
# print(Toyota.current_speed)

"""
Задача 2. Семья
Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома»
и объекты которого могут выполнять следующие действия:
- Отобразить информацию о себе.
- Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
- Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
    Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
Создайте как минимум один экземпляр класса и проверьте работу методов.

Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
> Family name: Common family
> Family funds: 100000
> Having a house: False

> Try to buy a house
> Not enough money!
 
> Earned 800000 money! Current value: 900000
> Try to buy a house again
> House purchased! Current money: 0.0
 
> Family name: Common family
> Family funds: 0.0
> Having a house: True
"""

#
# class Family:
#     surname = 'Common-family'
#     family_money = 100000
#     having_house = False
#
#     def info(self):
#         print(f'Family name: {self.surname}\n'
#               f'Family funds: {self.family_money}\n'
#               f'Having a house: {self.having_house}\n')
#
#     def earn_money(self, income_money):
#         self.family_money += income_money
#         print(f'Earned money: {income_money}! Current funds: {self.family_money}\n')
#
#     def buy_house(self, house_price, discount=0):
#         house_price -= house_price * discount / 100
#         if self.family_money >= house_price:
#             self.family_money -= house_price
#             self.having_house = True
#             print(f'House purchased! Current funds: {self.family_money}\n')
#         else:
#             print('Not enough money...\n')
#
#
# my_family = Family()
# my_family.info()
#
# print('Try to buy a house')
# my_family.buy_house(1000000)
# if not my_family.having_house:
#     my_family.earn_money(800000)
#     print('Try to buy house again')
#     my_family.buy_house(1000000, 10)
#     my_family.info()


"""
Задача 1. Машина 3
Вам предстоит снова немного видоизменить класс Toyota из прошлого урока.
На всякий случай вот описание класса.

Четыре атрибута:
- цвет машины (например, красный),
- цена (один миллион),
- максимальная скорость (200),
- текущая скорость (ноль).

Два метода:
- Отображение информации об объекте класса.
- Метод, который позволяет устанавливать текущую скорость машины.
Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса
(то есть передаваться в init). Реализуйте такое изменение класса.
"""

#
# class Toyota:
#
#     def __init__(self, car_color, car_price, max_speed, current_speed=0):
#         self.car_color = car_color
#         self.car_price = car_price
#         self.max_speed = max_speed
#         self.current_speed = current_speed
#
#     def info(self):
#         print(f'car color: {self.car_color}\n'
#               f'car price: {self.car_price}\n'
#               f'car max speed: {self.max_speed}\n'
#               f'current speed: {self.current_speed}\n')
#
#     def set_current_speed(self, speed):
#         self.current_speed = speed
#
#
# my_car = Toyota('gray', 200, 300, 36)
# my_car.info()


"""
Задача 2. Координаты точки
Объект «Точка» на плоскости имеет координаты X и Y.
При создании новой точки могут передаваться пользовательские значения координат,
по умолчанию x = 0, y = 0. 
Реализуйте класс, который будет представлять эту точку,
и напишите метод, который предоставляет информацию о ней.
Также внутри класса пропишите счётчик, который будет отвечать за количество созданных точек.
Подсказка: счётчик можно объявить внутри самого класса и увеличивать его в методе __init__.
"""

#
# class Point:
#     counter = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.counter += 1
#
#     def info(self):
#         print(f'x: {self.x}\n'
#               f'y: {self.y}\n'
#               f'counter: {self.counter}\n')
#
#
# point_1 = Point(5, 4)
# point_1.info()
# point_2 = Point(1, 6)
# point_1.info()
# point_2.info()


"""
Задача 3. Весёлая ферма
Для игры «Весёлая ферма» необходимо прописать два класса:
- класс «Картошка»
- класс «Грядка картошки».

У картошки есть:
- её номер в грядке
- стадия зрелости
Она может предоставлять информацию о своей зрелости и расти.
Всего у картошки может быть четыре стадии зрелости.

Грядка с картошкой содержит:
- список картошки, которая на ней растёт,
- может, собственно, взращивать всю эту картошку,
- предоставлять информацию о зрелости всей картошки на своей территории.

Реализуйте оба класса и проверьте их работу:
создайте экземпляр грядки из пяти картошек и три раза взрастите грядку.

Пример результата (проверка на зрелость и три взращивания):
> Картошка ещё не созрела!

> Картошка прорастает!

> Картошка 1 сейчас Росток
> Картошка 2 сейчас Росток
> Картошка 3 сейчас Росток
> Картошка 4 сейчас Росток
> Картошка 5 сейчас Росток
> Картошка ещё не созрела!

> Картошка прорастает!

> Картошка 1 сейчас Зелёная
> Картошка 2 сейчас Зелёная
> Картошка 3 сейчас Зелёная
> Картошка 4 сейчас Зелёная
> Картошка 5 сейчас Зелёная
> Картошка ещё не созрела!

> Картошка прорастает!

> Картошка 1 сейчас Зрелая
> Картошка 2 сейчас Зрелая
> Картошка 3 сейчас Зрелая
> Картошка 4 сейчас Зрелая
> Картошка 5 сейчас Зрелая
> Вся картошка созрела. Можно собирать!
"""


class Potato:
    states = {0: 'not yet', 1: 'sprout', 2: 'green', 3: 'ripe'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Potato {self.index} is {Potato.states[self.state]} now')


class PotatoGarden:

    def __init__(self, amount):
        self.potatoes = [Potato(index) for index in range(1, amount + 1)]

    def grow_all(self):
        print('\nThe potato is sprouting!\n')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            print('The potatoes are not ripe!\n')
            return False    # такой return поможет получить информацию
                            # о зрелости картошкиснаружи этого объекта
        else:
            print('All the potatoes are ripe. You can collect!\n')
            return True

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()


garden = PotatoGarden(5)
for _ in range(3):
    garden.grow_all()

garden.are_all_ripe()





