
# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


   #
  ###
 #####
#######

size = int(input('Enter the height: '))

my_list = list()


# for row in range(size):
#     for col in range(1, size * 2):
#         my_list.append(size + row)
#         my_list.append(size - row)
#         # if col == size:
#         #     print('#', end='')
#         if col in my_list:
#             print('#', end='')
#         else:
#             print(' ', end='')
#
#     print()

for i in range(0, size):
    print(" " * (size - i - 1), end='')
    print("#" * (2*i + 1), end='')
    print(" " * (size - i - 1))
