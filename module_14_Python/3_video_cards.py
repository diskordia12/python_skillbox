"""
Задание 3. Видеокарты
Что нужно сделать
В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений.
Вместо полных названий хранятся только числа, которые обозначают модель и поколение видеокарты.
Недавно компания выпустила новую линейку видеокарт. Самые старшие поколения разобрали за пару дней.
Напишите программу, которая удаляет наибольшие элементы из списка видеокарт.

Пример:
> Количество видеокарт: 5
> Видеокарта 1: 3070
> Видеокарта 2: 2060
> Видеокарта 3: 3090
> Видеокарта 4: 3070
> Видеокарта 5: 3090

> Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
> Новый список видеокарт: [ 3070 2060 3070 ]
"""

cards_amount = int(input('Enter amount of video cards: '))
video_cards = list()

for i in range(cards_amount):
    video_cards.append(int(input(f'Video card {i + 1}: ')))

print(f'Old list of video cards: {video_cards}')
oldest_card = max(video_cards)

while oldest_card in video_cards:
    video_cards.remove(oldest_card)

print(f'New list of video cards: {video_cards}')
