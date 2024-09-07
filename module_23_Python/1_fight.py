"""
Задача 1. Драка
Вы работаете в команде разработчиков мобильной игры, и вам досталась часть от ТЗ заказчика.
Есть два юнита, каждый называется «Воин».
Каждому устанавливается здоровье в 100 очков.
Они бьют друг друга в случайном порядке.
Тот, кто бьёт, здоровье не теряет.
У того, кого бьют, оно уменьшается на 20 очков от одного удара.
После каждого удара надо выводить сообщение,
какой юнит атаковал и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья,
программа завершается сообщением о том, кто одержал победу.
"""


import random


class Warrior:

    def __init__(self, name: str, health=100):
        self.unit_name = name
        self.health = health

    def punch(self):
        print(f'{self.unit_name} attacked')

    def got_punch(self):
        self.health -= 20
        print(f'{self.unit_name} has {self.health} health\n')

    def check_health(self):
        return self.health > 0


warrior_1 = Warrior('Godzilla')
warrior_2 = Warrior('Fluffy')

while warrior_1.check_health() and warrior_2.check_health():
    turn_for_punch = random.randint(1, 2)
    if turn_for_punch == 1:
        warrior_1.punch()
        warrior_2.got_punch()
    else:
        warrior_2.punch()
        warrior_1.got_punch()

if warrior_1.check_health():
    print(f'{warrior_1.unit_name} won!')
else:
    print(f'{warrior_2.unit_name} won!')
