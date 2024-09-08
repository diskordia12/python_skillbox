"""
Задача 3. Файлы и папки
Напишите программу, которая получает на вход путь до каталога
(в том числе это может быть просто корень диска) и выводит общее количество файлов и
подкаталогов в нём. Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).

Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех
вложенных в него файлов.

Результат работы программы на примере python_basic\Module14:
> E:\PycharmProjects\python_basic\Module14
> Размер каталога (в Кбайтах): 8.373046875
> Количество подкаталогов: 7
> Количество файлов: 15

"""

import os


def find_file(cur_path):
    amount_of_files = 0
    amount_of_directory = 0
    common_size = 0

    # print(cur_path)
    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        if os.path.isfile(path):
            amount_of_files += 1
            common_size += os.path.getsize(path)
        else:
            amount_of_directory += 1
            f, d, s = find_file(path)
            amount_of_files += f
            amount_of_directory += d
            common_size += s

    return amount_of_files, amount_of_directory, common_size


my_path = os.path.abspath(os.curdir)
print(my_path)


amount_of_files, amount_of_directory, common_size = find_file(my_path)
print(f'Amount of files: {amount_of_files}')
print(f'Amount of directories: {amount_of_directory}')
print(f'Size in kilobytes {common_size / 1024}')


