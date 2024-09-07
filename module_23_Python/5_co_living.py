"""
Задача 5. Совместное проживание
Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве,
Артём решил провести необычное исследование.
Для этого он реализовал модель человека и модель дома.

Человек может (должны быть такие методы):
- есть (+ сытость, − еда);
- работать (− сытость, + деньги);
- играть (− сытость);
- ходить в магазин за едой (+ еда, − деньги);
- прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).

У человека есть (должны быть такие атрибуты):
- имя,
- степень сытости (изначально 50),
- дом.

В доме есть: 
- холодильник с едой (изначально 50 еды), 
- тумбочка с деньгами (изначально 0 денег).

Если сытость человека становится меньше нуля, человек умирает.

Логика действий человека определяется следующим образом:
- Генерируется число кубика от 1 до 6.
- Если сытость < 20, то нужно поесть.
- Иначе, если еды в доме < 10, то сходить в магазин.
- Иначе, если денег в доме < 50, то работать.
- Иначе, если кубик равен 1, то работать.
- Иначе, если кубик равен 2, то поесть.
- Иначе играть.
По такой логике эксперимента человеку надо прожить 365 дней.

Реализуйте такую программу и создайте двух людей, живущих в одном доме.
Проверьте работу программы несколько раз. 

Советы и рекомендации
Глобальные переменные создают зависимости.
Чем больше класс обращается к переменным, созданным снаружи класса,
тем больше в классе появляется неопределённости
(для работы с классом вам придётся отслеживать значения всех этих переменных).
По возможности передавайте нужные данные в объект и записывайте их в атрибуты вместо
обращения к глобальной переменной.
"""
import random


class Home:

    def __init__(self, fridge=50, money=0):
        self.fridge = fridge
        self.money = money

    def get_money(self):
        return self.money

    def add_food(self, food_amount=50):
        self.fridge += food_amount

    def extract_food(self, food_amount=10):
        self.fridge -= food_amount

    def add_money(self, money_amount=40):
        self.money += money_amount

    def spend_money(self, money_amount=5):
        self.money -= money_amount

    def __str__(self):
        return f'Food: {self.fridge}  Money in bedside table: {self.money}'


class Person:
    home: Home  # pro typeHint for own classes

    def __init__(self, name: str, home: Home, fullness=50):
        self.name = name
        self.home = home
        self.fullness = fullness

    @property
    def alive(self):
        return self.fullness > 0

    def eat(self, food_amount=10):
        self.home.extract_food(food_amount)
        self.fullness += food_amount

    def work(self, money_amount=10):
        self.fullness -= 10
        self.home.add_money(money_amount)

    def play(self):
        self.fullness -= 10

    def go_shopping(self, food_amount=10, money_amount=10):
        if self.home.get_money() < 5:
            return False
        self.home.add_food(food_amount)
        self.home.spend_money(money_amount)
        return True

    def __str__(self):
        return (f'Person {self.name}:\nFullness - {self.fullness}\n'
                f'and has {self.home}')


def live_a_day(person: Person):
    lucky_number = random.randint(1, 6)
    if person.fullness < 20:
        person.eat()
    elif person.home.fridge < 10:
        if not person.go_shopping():
            person.work()
    elif person.home.money < 50:
        person.work()
    elif lucky_number == 1:
        person.work()
    elif lucky_number == 2:
        person.eat()
    else:
        person.play()


def life(people: list):
    day = 0
    while len(people) > 0 and day < 365:
        day += 1
        for person in people:
            if not person.alive:
                print(f'{person.name} died after {day - 1}')
                people.remove(person)
            live_a_day(person)

    print(f'People made it for {day} days')


my_house = Home()
couple_people = [Person('Nick', my_house), Person('Sally', my_house)]

life(couple_people)
for person in couple_people:
    print(person, end='\n\n')

