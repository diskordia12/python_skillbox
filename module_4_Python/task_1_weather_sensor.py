print('Задача 1. Датчик погоды')

# В за окном квартиры стоит датчик погоды, который определяет, идёт ли дождь. Если идёт, датчик оповещает сообщением: «Пошёл дождь. Возьмите зонтик!»

# Напишите программу, которая получает на вход число 0 или 1. Единица означает, что дождь идёт. В таком случае выводите на экран сообщение: «Пошёл дождь. Возьмите зонтик!». Ноль означает, что дождя нет, в этом случае надо вывести сообщение «Дождя нет!»

# Пример 1:
# На улице идёт дождь? 1
# Пошёл дождь. Возьмите зонтик!

# Пример 2:
# На улице идёт дождь? 0
# Дождя нет!

rain_marker = int(input('Rain marker value: '))
if rain_marker == 1:
    print('Rain is coming. Take an umbrella!')
else:
    print('No rain!')
