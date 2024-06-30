# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|

width = int(input('Enter the width of a frame: '))
height = int(input('Enter the height of a frame: '))

for row in range(height):
    for col in range(width):
        if row == 0 or row == height - 1:
            print('-', end='')
        elif col == 0 or col == width - 1:
            print('|', end='')
        else:
            print(' ', end='')
    print()
    