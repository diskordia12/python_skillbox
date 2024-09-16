"""
Задача 1. Координаты точки
В одной из практик предыдущего модуля была задача на реализацию класса «Точка».
Модернизируйте класс по следующему условию:
объект «Точка» на плоскости имеет координаты x и y;
при создании новой точки могут передаваться пользовательские значения координат,
по умолчанию x = 0, y = 0.

Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:
- Предоставление информации о точке (используйте магический метод str).
- Геттер и сеттер для x.
- Геттер и сеттер для y.
Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.
"""
#
#
# class Dot:
#
#     def __init__(self, x=0, y=0):
#         self._x = self.set_x(x)
#         self._y = self.set_y(y)
#
#     def __str__(self):
#         return f'({self._x}, {self._y})'
#
#     def get_x(self):
#         return self._x
#
#     def get_y(self):
#         return self._y
#
#     # @staticmethod
#     # def check_value(value):
#     #     if isinstance(value, str):
#     #         try:
#     #             value = float(value)
#     #         return True
#     #     if isinstance(value, (int, float)):
#     #         return True
#     #     return False
#
#     def set_x(self, x):
#         try:
#             x = float(x)
#         except ValueError as e:
#             print(e, ' - x must be digit')
#
#         self._x = x
#         return x
#
#     def set_y(self, y):
#         try:
#             y = float(y)
#         except ValueError as e:
#             print(e, ' - x must be digit')
#
#         self._y = y
#         return self._y
#
#
# my_dot = Dot()
# print(my_dot)
# my_dot.set_x(5)
# my_dot.set_y('6.7')
# print(my_dot)


"""
Задача 2. Человек
Реализуйте класс «Человек», который инициализируется именем
(имя должно состоять только из букв) и возрастом (должен быть в диапазоне от 0 до 100),
а внутри класса считается общее количество инициализированных объектов.
Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических),
а для изменения и получения данных объекта напишите специальные геттеры и сеттеры. 

При тестировании класса измените приватный атрибут (например, возраст) двумя способами:
сеттером и «крайне не рекомендуемым», который был показан в уроке.
"""

#
# class Human:
#
#     _count = 0
#
#     def __init__(self, name, age):
#         self._name = ''
#         self._age = 0
#         self.set_age(age)
#         self.set_name(name)
#         Human._count += 1
#
#     def __str__(self):
#         return f'Name: {self._name} Age: {self._age}'
#
#     def get_count(self):
#         return self._count
#
#     def get_name(self):
#         return self._name
#
#     def get_age(self):
#         return self._age
#
#     def set_name(self, name: str):
#         if name.isalpha():
#             self._name = name
#         else:
#             raise ValueError('Name must contain only letters')
#
#     def set_age(self, age: int):
#         if isinstance(age, (float, int)) and age in range(0, 100 + 1):
#             self._age = age
#         else:
#             raise ValueError('Age must be from 0 to 100')
#
#
# my_person = Human('kate', 16)
# print(my_person)
# print(my_person.get_count())
#
# human = Human('helo', 100)  # значения передадутся в сеттер
# print(human)
# human._age = 99  # «крайне не рекомендуемый» метод
# print(human)
# print(my_person.get_count())


"""
Задача 1. Автомобили
Даны два класса автомобилей: грузовой и легковой.
У каждого из этих автомобилей есть своя модель, и каждый может сделать два действия:
сообщить свою модель и поехать.

Грузовой автомобиль имеет такой атрибут, как заполненность багажника, изначально он равен нулю.
У него есть ещё два действия: загрузить и разгрузить багажник.

У легкового автомобиля нет багажника, но есть навигационная система,
которая передаётся вместе с моделью.
Также вместо загрузки и разгрузки у него есть другое действие — включить навигацию.

Реализуйте классы грузового и легкового автомобилей.
Для этого выделите общие атрибуты и методы в отдельный класс «Автомобиль»
и используйте наследование. Не забудьте о функции super в дочерних классах.
"""
#
#
# class Car:
#
#     def __init__(self, model: str):
#         self.model = model
#
#     def __str__(self):
#         return self.model
#
#     def move(self):
#         return f'Car model: {self.model} started to move'
#
#
# class CargoCar(Car):
#
#     def __init__(self, model: str, trunk_capacity=0):
#         super().__init__(model)
#         self.trunk_capacity = trunk_capacity
#
#     def __str__(self):
#         return f'Car {self.model}\nCurrently trunk capacity: {self.trunk_capacity}'
#
#     @property
#     def capacity(self):
#         return self.trunk_capacity
#
#     def load_trunk(self, weight: float):
#         if self.trunk_capacity + weight < 30:
#             self.trunk_capacity += weight
#         else:
#             print('The trunk is full')
#
#     def unload_trunk(self, weight=capacity):
#         if self.trunk_capacity == 0:
#             print('Trunk is already empty')
#         else:
#             self.trunk_capacity -= weight
#
#
# class PassengerCar(Car):
#
#     def __init__(self, model: str, gps: str):
#         super().__init__(model)
#         self.gps = gps
#
#     def turn_on_gps(self):
#         return f'GPS {self.gps} in car {self} turned on'
#
#
# cargo_car = CargoCar('Cargo car', 5)
# print(cargo_car)
# print(cargo_car.load_trunk(60))
# print(cargo_car.move())
# print()
#
# passanger_car = PassengerCar('passenger car', 'globalGPS')
# print(passanger_car)
# print(passanger_car.turn_on_gps())


"""
Задача 2. Домашние роботы
На выставку робототехники привезли несколько интересных моделей роботов,
которые похожи между собой, но немного различаются функциональностью.
У каждого робота есть номер модели и действие operate,
которое описывает выполняемые им функции.

Особенности роботов:
- У робота-пылесоса есть мешок для мусора, изначально он пустой (0).
    При команде operate робот сообщает, что он пылесосит пол,
    и выводит текущую заполняемость мешка.
- У робота-охранника есть сигнализация, и при команде operate он выводит сообщение
    о патрулировании дома с её помощью.
- Ещё есть робот для бассейнов, который также является охранником.
    У этого робота есть значение глубины, и при команде operate он делает то же,
    что и робот-охранник, плюс сообщает, что охрана ведётся под водой.
Напишите программу, которая реализует все необходимые классы роботов.
"""
#
#
# class Robot:
#
#     def __init__(self, model: str):
#         self.model = model
#
#     def __str__(self):
#         return self.model
#
#     def operate(self):
#         pass
#
#
# class RobotVacuumCleaner(Robot):
#
#     def __init__(self, model: str, garbage_bag=0):
#         super().__init__(model)
#         self.garbage_bag = garbage_bag
#
#     def operate(self):
#         self.garbage_bag += 1
#         return f'Robot {self} is vacuuming now. Garbage bag: {self.garbage_bag}'
#
#
# class SecurityRobot(Robot):
#
#     def __init__(self, model: str, alarm: str):
#         super().__init__(model)
#         self.alarm = alarm
#
#     def operate(self):
#         return f'Robot {self} is patrolling home with alarm {self.alarm}'
#
#
# class RobotPool(SecurityRobot):
#
#     def __init__(self, model: str, alarm: str, deep: int):
#         super().__init__(model, alarm)
#         self.deep = deep
#
#     def operate(self):
#         print(super().operate())
#         return f'Patrol is {self.deep} meters under the water'
#
#
# robot_one = RobotVacuumCleaner('cleaner3000', 4)
# for _ in range(4):
#     print(robot_one.operate())
# print()
#
# robot_two = SecurityRobot('security2000', 'superAlarm')
# print(robot_two.operate())
# print()
#
# robot_three = RobotPool('pool3000', 'underAlarm', 5)
# print(robot_three.operate())
# print()


"""
Задача 3. Кастомные исключения
Исключения в Python также являются классами, и все они берут свои истоки от самого
главного класса — Exception.
И для создания своего собственного класса ошибки достаточно написать его дочерний класс.
Например:

class MyOwnException(Exception):
    pass

raise MyOwnException('Это моя ошибка!')

Причём содержимое объекта исключения чаще всего так и оставляют (просто pass),
чтобы не сломать автоматические обработчики исключений.
Напишите программу, которая считывает из файла numbers.txt пары чисел,
делит первое число на второе и выводит ответ на экран.
Если первое число меньше второго, то программа выдаёт исключение
DivisionError (нельзя делить меньшее на большее). 
Дополнительно, с помощью try except, можно обработать исключение на своё усмотрение.
"""

#
# class DivisionError(Exception):
#     def __str__(self):
#         return 'you cannot divide less by more'
#
#
# numbers = [(1, 2), (4, 1), (88, 2), (2, 0), (0, 5)]
#
# for pair in numbers:
#     try:
#         if pair[0] < pair[1]:
#             raise DivisionError
#         print(f'{pair[0]}/{pair[1]} = {pair[0] / pair[1]}')
#     except (ValueError, ZeroDivisionError, DivisionError) as e:
#         print(e, type(e), pair[0], pair[1])


"""
Задача 1. Юниты
Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты).
У Юнита есть действие «получить урон» (базовый класс получает 0 урона).

Также есть два дочерних класса:
- Солдат: получает урон, равный переданному значению.
- Обычный гражданин: получает урон, равный двукратному переданному значению. 
Реализуйте родительский и дочерние классы и их методы,
используя принцип полиморфизма (а также инкапсуляции и наследования, конечно же).
"""
#
#
# class Unit:
#
#     def __init__(self, hp: int):
#         self._hp = hp
#
#     def get_hp(self):
#         return self._hp
#
#     def set_hp(self, amount):
#         self._hp = amount
#
#     def get_damage(self, amount):
#         self.set_hp(self.get_hp() - 0)
#
#
# class Soldier(Unit):
#
#     def get_damage(self, amount):
#         self.set_hp(self.get_hp() - amount)
#
#
# class Citizen(Unit):
#
#     def get_damage(self, amount):
#         self.set_hp(self.get_hp() - 2 * amount)
#
#
# soldier = Soldier(hp=80)
# soldier.get_damage(amount=50)
# print(soldier.get_hp())
#
# citizen = Citizen(hp=80)
# citizen.get_damage(amount=50)
# print(citizen.get_hp())


"""
Задача 2. Полёт
Иногда для реализации дочерних классов используется так называемый класс-роль,
где также описываются общие атрибуты и методы,
но в программе инициализируются объекты только дочерних классов,
а базовый класс-роль не трогается.
К примеру, что общего у бабочки и ракеты? Они обе могут летать и приземляться. 

Реализуйте класс «Может летать». 
Атрибуты:
- Высота = 0.
- Скорость = 0.
Методы:
- Взлететь (в теле прописать pass).
- Лететь (в теле прописать pass).
- Приземлиться (установить высоту и скорость в значение 0).
Вывести высоту и скорость на экран.
 

Затем реализуйте два дочерних класса: 

«Бабочка», который может:
- Взлететь (высота = 1).
- Лететь (скорость = 0.5).

«Ракета», которая может:
- Взлететь (высота = 500, скорость = 1000).
- Приземлиться (высота = 0, взрыв).
- Взорваться (тут уже что угодно).
"""
#
#
# class Fly:
#
#     def __init__(self, height=0, speed=0):
#         self.height = height
#         self.speed = speed
#
#     def take_off(self):
#         pass
#
#     def fly(self):
#         pass
#
#     def land(self):
#         self.height = 0
#         self.speed = 0
#
#     def __str__(self):
#         return f'Height: {self.height}\tSpeed: {self.speed}'
#
#
# class Butterfly(Fly):
#
#     def take_off(self):
#         self.height = 1
#
#     def fly(self):
#         self.speed = 0.5
#
#
# class Aircraft(Fly):
#
#     def explosion(self):
#         self.height = 0
#         self.speed = 0
#         print('Aircraft exploded')
#
#     def take_off(self):
#         self.height = 500
#         self.speed = 100
#
#     def land(self):
#         self.height = 0
#         self.explosion()
#
#
# aircraft = Aircraft()
# print(aircraft.take_off())
# print(aircraft)
# print(aircraft.land())


from binarytree import Node

# Создание бинарного дерева вручную
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

# Вывод структуры дерева
print("Структура бинарного дерева:")
print(root)

# Обход дерева в прямом порядке (preorder)
def preorder(node):
    if node is not None:
        print(node.value)
        preorder(node.left)
        preorder(node.right)

print("Обход дерева в прямом порядке (preorder):")
preorder(root)


# Поиск элемента в дереве
def search(node, value):
    if node is None or node.value == value:
        return node
    if value < node.value:
        return search(node.left, value)
    return search(node.right, value)


print("Поиск элемента в дереве:")
result = search(root, 7)
if result is not None:
    print("Элемент найден!")
else:
    print("Элемент не найден!")







