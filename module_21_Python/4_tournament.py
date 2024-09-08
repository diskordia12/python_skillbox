"""
Задача 4. Турнир
В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре «Орлеан»:
фамилии, имена и количество баллов, набранных в первом туре.
Во второй тур проходят участники, которые набрали более K баллов в первом туре.

Напишите программу, которая выводит в файл second_tour.txt данные всех участников,
прошедших во второй тур, с нумерацией.
В первой строке нужно вывести в файл second_tour.txt количество участников второго тура.
Затем программа должна вывести фамилии, инициалы и количество баллов всех участников,
прошедших во второй тур, с нумерацией.
Имя нужно сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.

Пример:
Содержимое файла first_tour.txt:
80
Ivanov Serg 80
Sergeev Petr 92
Petrov Vasiliy 98
Vasiliev Maxim 78

Содержимое файла second_tour.txt:
2
1) V. Petrov 98
2) P. Sergeev 92
"""

import os


all_players = list()

with open(os.path.join(os.curdir, 'first_tour.txt'), 'r') as first_tour_file:
    threshold = first_tour_file.readline()
    # first_tour_file.seek(len(threshold))  # Redundant, because I've already mover cursor

    for player in first_tour_file:
        all_players.append(tuple(player.split()))

print(all_players)

players_of_second_tour = [(name[0] + '.', surname, score)
                            for surname, name, score in all_players if int(score) > int(threshold)]
# for player in all_players:
#     points = int(player[2])
#     if points > int(threshold):
#         name_initial = player[1][0] + '.'
#         players_of_second_tour.append((name_initial, player[0], str(points)))

# print(sorted(players_of_second_tour, key=lambda elem: elem[2], reverse=True))
players_of_second_tour.sort(key=lambda elem: elem[2], reverse=True)

with open(os.path.join(os.curdir, 'second_tour.txt'), 'w') as second_tour_file:
    second_tour_file.write(str(len(players_of_second_tour)) + '\n')
    for player in players_of_second_tour:
        name, surname, points = player
        second_tour_file.write(' '.join(player))
        second_tour_file.write('\n')


print(players_of_second_tour)
