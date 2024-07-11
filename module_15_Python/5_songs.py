"""
Задача 5. Песни
Мы пишем приложение для удобного прослушивания музыки.
У Вани есть список из девяти песен группы Depeche Mode.
В информацию о каждом треке входит название и продолжительность с точностью до долей минут:

violator_songs = [
                        ['World in My Eyes', 4.86],
                        ['Sweetest Perfection', 4.43],
                        ['Personal Jesus', 4.56],
                        ['Halo', 4.9],
                        ['Waiting for the Night', 6.07],
                        ['Enjoy the Silence', 4.20],
                        ['Policy of Truth', 4.76],
                        ['Blue Dress', 4.29],
                        ['Clean', 5.83]
                ]

Из этого списка Ваня хочет выбрать N песен и добавить их в особый плейлист с другими треками.
При этом ему важно, сколько времени в сумме эти N песен будут звучать.
Напишите программу, которая запрашивает у пользователя количество песен из списка и их названия,
а на экран выводит общее время их звучания.

Пример:
> Сколько песен выбрать? 3
> Название 1-й песни: Halo
> Название 2-й песни: Enjoy the Silence
> Название 3-й песни: Clean
> Общее время звучания песен — 14,93 минуты
"""

violator_songs = [
                        ['World in My Eyes', 4.86],
                        ['Sweetest Perfection', 4.43],
                        ['Personal Jesus', 4.56],
                        ['Halo', 4.9],
                        ['Waiting for the Night', 6.07],
                        ['Enjoy the Silence', 4.20],
                        ['Policy of Truth', 4.76],
                        ['Blue Dress', 4.29],
                        ['Clean', 5.83]
                ]

violator_songs = dict(violator_songs)

amount_of_songs = int(input('How many songs to add: '))
playing_time = 0

for i in range(amount_of_songs):
    song_name = input(f'Name of {i + 1} song: ')
    playing_time += violator_songs[song_name]

playing_time = round(playing_time, 2)
print(f'Total playing time of songs: {playing_time} min')
