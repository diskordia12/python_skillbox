"""
Задача 1. Сумма чисел 2
Что нужно сделать
Во входном файле numbers.txt записано N целых чисел,
которые могут быть разделены пробелами и концами строк.
Напишите программу, которая выводит сумму чисел во выходной файл answer.txt.

Пример:
Содержимое файла numbers.txt
     2
2
  2
        2

Содержимое файла answer.txt
8
"""


import os


# def get_sum(path_to_file: str):
#     sum_numbers = 0
#     with open(path_to_file, "r", encoding="utf8") as file:
#         for line in file:
#             for sym in line:
#                 if sym.isdigit():
#                     sum_numbers += int(sym)
#     return sum_numbers


def get_sum(path_to_file: str):
    sum_numbers = 0
    with open(path_to_file, "r", encoding="utf8") as file:
        for line in file:
            clear_line = line.strip()
            if clear_line.isdigit():
                sum_numbers += int(clear_line)
    return sum_numbers


my_path = os.path.abspath(os.path.join(os.curdir, 'numbers.txt'))
answer_path = os.path.abspath(os.path.join(os.curdir, 'answer.txt'))

with open(answer_path, 'w') as answer_file:
    sum_of_numbers = get_sum(my_path)
    answer_file.write(str(sum_of_numbers))
