"""
Задача 6. Абстрактный класс
Вы работаете в компании, занимающейся разработкой программного обеспечения для
архитектурных проектов. Вам необходимо разработать программу для расчёта площади
различных геометрических фигур, таких как круги, прямоугольники и треугольники.

Задача
Создайте:
- класс Shape, который будет базовым классом для всех фигур и будет хранить пустой метод area,
    который наследники должны переопределить;
- класс Circle;
- класс Rectangle;
- класс Triangle.
Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод
для вычисления площади фигуры.
Дополнительно: изучите информацию о работе с абстрактными классами.

На основе этой информации сделайте так, чтобы:
- Нельзя было создавать объекты класса Shape.
- Наследники класса Shape переопределяли его метод area,
чтобы объекты этих классов можно было использовать.
"""

from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, name: str, r: float):
        super().__init__(name)
        self.radius = r

    def area(self):
        return pi * self.radius * self.radius

    def __str__(self):
        return f'{self.name} area is {self.area()}'


class Rectangle(Shape):

    def __init__(self, name: str, length: float, width: float):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f'{self.name} area is {self.area()}'


class Triangle(Shape):

    def __init__(self, name: str, a_side: float, b_side: float, c_side: float):
        super().__init__(name)
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def area(self):
        p = self.a_side + self.b_side + self.c_side
        return sqrt(p * (p - self.a_side) * (p - self.b_side) * (p - self.c_side))

    def __str__(self):
        return f'{self.name} area is {self.area()}'


circle = Circle('Circle', 5)
print(circle)

rectangle = Rectangle('Rectangle', 5, 3)
print(rectangle)

triangle = Triangle('Triangle', 10, 2, 5)
print(triangle)

