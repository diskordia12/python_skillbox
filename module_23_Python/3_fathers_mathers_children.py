"""
Задача 3. Отцы, матери и дети
Реализуйте два класса: «Родитель» и «Ребёнок».
У родителя есть:
- имя,
- возраст,
- список детей.

И он может:
- сообщить информацию о себе,
- успокоить ребёнка,
- покормить ребёнка.

У ребёнка есть:
- имя,
- возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
- состояние спокойствия,
- состояние голода.
Реализация состояний — на ваше усмотрение.
Это может быть и простой «флаг», и словарь состояний, и что-то поинтереснее.
"""

import random
from typing import List  # for adding pro typeHints for own classes


class Child:

    def __init__(self, name: str, age: int, state_calm=True, state_hungry=True):
        # True - calm/full, False -crying/hungry
        self.name = name
        self.age = age
        self.state_calm = state_calm
        self.state_hungry = state_hungry

    def info(self):
        print(f'Child {self.name} is {self.age} years old')
        if self.state_calm:
            print('Child is calm now')
        else:
            print('Child is crying')

        if self.state_hungry:
            print('Child is not hungry now\n')
        else:
            print('Child is hungry\n')


class Parent:

    children: List[Child]  # pro typeHint for own classes

    def __init__(self, name: str, age: int, children=None):
        self.name = name
        self.age = age
        self.children = [] if children is None else children

    def info(self):
        print(f'{self.name} {self.age} years old has {len(self.children)} children\n')
        for child in self.children:
            child.info()
        print()

    def calm_child(self, child: Child):
        if child.state_calm:
            print(f'{child.name} is already calm')
        else:
            print(f'{self.name} calms the {child.name} now')
            child.state_calm = True

    def feed_child(self, child: Child):
        if child.state_hungry:
            print(f'{child.name} is full')
        else:
            print(f'{self.name} feeds the {child.name} now')
            child.state_hungry = True


parent_name = input('Enter parent name: ')
parent_age = int(input('Enter parent age: '))
parent = Parent(parent_name, parent_age)

children_count = int(input('How many children: '))
for i in range(children_count):
    child_name = input(f'Enter name of {i + 1} child: ')
    child_age = int(input(f'Enter age of {i + 1} child: '))

    try:
        if parent_age - child_age < 16:
            raise ValueError('It can\'t be your child.\n'
                             'You must have at least 16 years gap between you and your child')
    except ValueError as e:
        print(e)

    child = Child(child_name, child_age)
    parent.children.append(child)

print(parent.info())

for kid in parent.children:
    kid.state_calm = random.randint(0, 1)
    kid.state_hungry = random.randint(0, 1)
    kid.info()
    parent.calm_child(kid)
    parent.feed_child(kid)
    print()



