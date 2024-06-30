# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

size = int(input('Enter the number for pit: '))
max_string_size = size * 2
start_string = ''
end_string = ''


for row in range(size, 0, -1):
    start_string += str(row)
    end_string = str(row) + end_string
    padding = '.' * (max_string_size - 2 * (size - row + 1))
    print(f'{start_string}{padding}{end_string}')

