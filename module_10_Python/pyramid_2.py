# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
# 1:             1
# 2:          3     5
# 3:       7     9     11
# 4:   13    15    17    19
# 5:21    23    25    27    29

size = int(input('Enter the size of pyramid: '))

space_length = len(str(((size + 1) * size + 1))) * 2 + 1

max_string_size = space_length * (size - 1) + size * 2

for row in range(1, size + 1):
    first_number = row * (row - 1) + 1
    odd_str = ''
    for i in range(0, row):
        odd_str += str(first_number + 2 * i)
        space = ' ' * (space_length - len(str(first_number + 2 * i)) + 1)
        if i != row - 1:
            odd_str += space
    padding = ' ' * ((max_string_size - len(odd_str)) // 2)
    print(f'{padding}{odd_str}{padding}')

