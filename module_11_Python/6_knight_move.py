
# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

x_1 = float(input(' Enter coordinate of x_1: '))
y_1 = float(input(' Enter coordinate of y_1: '))

x_2 = float(input(' Enter coordinate of x_2: '))
y_2 = float(input(' Enter coordinate of y_2: '))


if 0 <= x_2 <= 0.8 and 0 <= y_2 <= 0.8:
    x_1_square = int(x_1 * 10)
    y_1_square = int(y_1 * 10)
    x_2_square = int(x_2 * 10)
    y_2_square = int(y_2 * 10)
    print(f'Knight is on ({x_1_square},{y_1_square}) cell. New cell is ({x_2_square},{y_2_square})')

    dx = abs(x_1_square - x_2_square)
    dy = abs(y_1_square - y_2_square)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        print('Yes, knight can move to this cell')
    else:
        print('No, knight can\'t move to this cell')
else:
    print('There is no cell with this coordinates')