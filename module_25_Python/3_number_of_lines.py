"""
Задача 3. Количество строк
Реализуйте функцию-генератор, которая берёт все питоновские файлы
в директории и вычисляет количество строк в каждом файле,
игнорируя пустые строки и строки комментариев.
По итогу функция-генератор должна с помощью yield каждый раз возвращать количество строк
в очередном файле.
"""

import os


def gen_number_of_file_lines(directory: str):
    for file in os.listdir(directory):
        lines_amount = 0
        if os.path.splitext(file)[1] == '.py':
            with open(file, 'r') as python_file:
                for line in python_file:
                    if not line.strip() == '' and not line.strip().startswith(('#', '"')):
                        lines_amount += 1
            yield file, lines_amount


my_path = os.path.abspath(os.path.join(os.pardir, 'module_25_Python'))
print(my_path)
for file, lines in gen_number_of_file_lines(my_path):
    print(f'file: {file} contains {lines} lines')
