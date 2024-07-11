"""
Задание 6. Ролики
Частная контора даёт в прокат ролики самых разных размеров.
Человек может надеть ролики только своего размера.
Пользователь вводит два списка размеров: N размеров роликов и K размеров ног людей.
Реализуйте код, который определяет, какое наибольшее число человек может одновременно взять ролики
и пойти кататься.

Пример:
> Количество роликов: 4
> Размер пары 1: 41
> Размер пары 2: 40
> Размер пары 3: 39
> Размер пары 4: 42

Количество людей: 3
> Размер ноги человека 1: 42
> Размер ноги человека 2: 41
> Размер ноги человека 3: 42
> Наибольшее количество людей, которые могут взять ролики: 2
"""


amount_of_rollers = int(input('Amount of rollers: '))
roller_sizes = list()

for i in range(amount_of_rollers):
    roller_sizes.append(input(f'Size {i + 1} pair of rollers: '))

amount_of_people = int(input('\nAmount of people: '))
people_sizes = list()

for i in range(amount_of_people):
    people_sizes.append(input(f'Size {i + 1} person: '))

people_with_rollers = 0
for i in people_sizes:
    if i in roller_sizes:
        people_with_rollers += 1
        roller_sizes.remove(i)

print(f'\nMost people who can borrow rollers: {people_with_rollers}')
