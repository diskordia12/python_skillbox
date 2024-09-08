# """
# Задача 1. Сисадмин
# Вы работаете системным администратором в одной компании.
# На диске каждого сотрудника компании в специальной папке access лежит файл admin.bat.
# Этот файл предназначен для вас, и вам нужен путь до этого файла,
# причём как относительный, так и абсолютный.
# Недолго думая, вы решили написать небольшой скрипт, который закинете по сети к этому файлу.
#
# Напишите программу, которая выводит на экран относительный и абсолютный пути до файла admin.bat.
#
# Пример результата:
# > Абсолютный путь до файла: C:\Users\Roman\PycharmProjects\Skillbox\access\admin.bat
# > Относительный путь до файла: Skillbox\access\admin.bat
# """

# import os
#
# abs_path = os.path.abspath('admin.bat')
# print(f'Abs path\n {abs_path}')
#
# rel_path = os.path.join("access", "admin.bat")
# abs_path = os.path.abspath(rel_path)
# print("Абсолютный путь до файла:", abs_path)
# print("Относительный путь до файла:", rel_path)

"""
Задача 2. Содержимое
Выберите любую директорию на своём диске и затем напишите программу, выводящую на экран абсолютные пути к файлам и папкам, которые находятся внутри этой директории.

Результат программы на примере директории проекта python_basic:

Содержимое каталога G:\PycharmProjects\python_basic

    G:\PycharmProjects\python_basic\.git

    G:\PycharmProjects\python_basic\.idea

    G:\PycharmProjects\python_basic\Module14

    G:\PycharmProjects\python_basic\Module15

    G:\PycharmProjects\python_basic\Module16

    G:\PycharmProjects\python_basic\Module17

    G:\PycharmProjects\python_basic\Module18

    G:\PycharmProjects\python_basic\Module19

    G:\PycharmProjects\python_basic\Module20

    G:\PycharmProjects\python_basic\Module21

    G:\PycharmProjects\python_basic\Module22
"""
#
# import os
#
#
# def print_dirs(directory: str):
#     print(f'\nDirectory {directory} contents:')
#     for file in os.listdir(directory):
#         print(f'\t{os.path.join(directory, file)}')
#
#
# path_to_directory = os.path.abspath(os.path.join(os.pardir, os.pardir, 'python_skillbox'))
# print_dirs(path_to_directory)
#
# print()
#
# for path in os.listdir('..'):
#     print(os.path.join(os.path.abspath('..'), path))


"""
Задача 3. Корень диска
Напишите программу, которая выводит на экран только корень диска, на котором запущен скрипт. Учтите, что скрипт может быть запущен где угодно и при любой вложенности папок.

Результат программы на примере диска G:

Корень диска: G:\\
"""

# import os
# import platform
#
# # Решение для Windows:
# if platform.system() == 'Windows':
#     print("Корень диска:", os.path.abspath(os.curdir).split(os.sep)[0])
# else: # UNIX-like
#     print("Корень диска:", os.sep)


# """
# Задача 1. Иконки
# Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура
# его диска: папки одними иконками, файлы — другими.
# Поэтому ему нужен код, который поможет определить, какой тип иконки вставить.
# Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь
# (на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение.
# Если путь указывает на файл, то также выведите его размер (сколько он весит в байтах).
# Обеспечьте контроль ввода: проверка пути на существование.
#
# Подсказка: для вывода размера файла поищите соответствующий метод.
#
#
#
# Пример 1:
# # > Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# > Это файл
# > Размер файла: 605 байт
#
# Пример 2:
# > Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# > Указанного пути не существует
# """
#
# import os
#
# my_path = os.path.abspath(os.path.join(os.curdir, 'main.py'))
# print(my_path)
#
# if os.path.exists(my_path):
#     if os.path.isdir(my_path):
#         print('This is directory')
#     elif os.path.isfile:
#         print('This is a file')
#         print(f'Size of the file: {os.path.getsize(my_path)} bait')
#     elif os.path.islink:
#         print('Path is a link')
#         print(f'Size of the file: {os.path.getsize(my_path)}')
#
# else:
#     print('This path does not exist')


"""
Задача 2. Поиск файла
В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории.
Однако, как мы понимаем, файлов с таким названием может быть несколько.

Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла,
проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.

 

Пример:
Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
Имя файла: lesson2
 
Найдены следующие пути:
C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
"""
#
# import os
#
#
# def find_files(current_path: str, file_name: str):
#     for elem in os.listdir(current_path):
#         path = os.path.join(current_path, elem)
#         if file_name == elem:
#             print(os.path.abspath(path))
#         if os.path.isdir(path):
#             result = find_files(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
#
# my_path = os.path.abspath(os.pardir)
# file_name = 'main.py'
# print(my_path)
# print(find_files(my_path, file_name))


# def find_file(cur_path, file_name):
#     print("Запуск поиска в папке", os.path.join(os.path.abspath(cur_path)))
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print("Проверяется путь", path)
#         if file_name == i_elem:
#             print(os.path.abspath(path))
#         elif os.path.isdir(path):
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
# find_file('..', 'test.py')


"""
Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей.
Файл первой группы (group_1.txt) находится в папке task,
файл второй группы (group_2.txt) — в папке Additional_info.
Содержимое файла group_1.txt
Бобровский Игорь 10
Дронов Александр 20
Жуков Виктор 30

Содержимое файла group_2.txt
Павленко Геннадий 20
Щербаков Владимир 35
Marley Bob 15

На экран нужно было вывести сумму очков первой группы,
затем разность очков опять же первой группы и напоследок — произведение очков уже второй группы. 

Программист оказался не очень опытным,
писал код наобум и даже не стал его проверять.
И оказалось, этот код просто не работает. Вот что он написал:

file = open('E:task\group_1.txt', 'read')

summa = 0
for i_line in file:
    info = i_line.split()
    summa += info[2]
file = open('E:task\group_1.txt', 'read')
diff = 0
for i_line in file:
    info = i_line.split()
    diff -= info[2]
file_2 = open('E:task\group_2.txt', 'read')
compose = 0
for i_line in file:
    info = i_line.split()
    compose *= info[2]
print(summa)
print(diff)
print(compose)

Исправьте код для решения поставленной задачи.
Для проверки результата создайте необходимые папки (task, Additional_info, Dont touch me)
на своём диске в соответствии с картинкой и также добавьте файлы group_1.txt и group_2.txt.
"""
#
# import os
#
#
# path_to_first = os.path.abspath(os.path.join('task', 'group_1.txt'))
# print(path_to_first)
#
# path_to_second = os.path.abspath(os.path.join('task', 'Additional_info', 'group_2.txt'))
# print(path_to_second)
#
# points_sum = 0
# points_diff = 0
# points_composition = 1
#
# with open(path_to_first, 'r', encoding='utf8') as first_file:
#     for line in first_file:
#         points_sum += int(line.split()[2])
#         points_diff -= int(line.split()[2])
#
# print(f'Sum of points: {points_sum}')
# print(f'Diff of points: {points_diff}')
#
# with open(path_to_second, 'r', encoding='utf8') as second_file:
#     for line in second_file:
#         points_composition *= int(line.split()[2])
#
# print(f'Composition of points in second file: {points_composition}')
#


"""
Задача 2. Поиск файла 2
Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту.
Таким образом, с ними можно работать точно так же, как и с обычными текстовыми файлами.
Используя функцию поиска файла из предыдущего урока, реализуйте программу,
которая находит внутри указанного пути все файлы с искомым названием и выводит на экран текст одного из них (выбор можно сгенерировать случайно).

Подсказка: можно использовать, например, список для сохранения найденного пути.
"""
#
# import os
# import random
#
#
# def find_file(cur_path, file_names):
#     all_paths = []
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if i_elem in file_names:
#             all_paths.append(os.path.abspath(path))
#         elif os.path.isdir(path):
#             result = find_file(path, file_names)
#             if result:
#                 all_paths.extend(result)
#
#     return all_paths
#
#
# def check_file_inside(path_to_file):
#     file = open(path_to_file, "r", encoding="utf8")
#     for line in file:
#         print(line)
#     file.close()
#
#
# all_paths = find_file(
#     os.pardir,
#     (
#         "1_challange_2.py",
#         "2_search_for_elem.py",
#         "3_deep_copy.py",
#     ),
# )
#
# print(all_paths)
#
# check_file_inside(random.choice(all_paths))
#

"""
Задача 1. Сумма чисел
Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
Напишите программу, которая выводит их сумму в выходной файл answer.txt.

Пример:
Содержимое файла numbers.txt:
1
2
3
4
10

Содержимое файла answer.txt
20
"""

# import os
#
# sum_of_numbers = 0
#
# with open(os.path.join(os.curdir, 'numbers.txt'), 'r') as numbers_file:
#     for num in numbers_file:
#         sum_of_numbers += int(num)
#
# with open(os.path.join(os.curdir, 'answer.txt'), 'w') as answer_file:
#     answer_file.write(str(sum_of_numbers))


"""
Задача 2. Всё в одном
Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город,
и там у него случилась беда: его диск пришлось отформатировать,
а доступ в интернет отсутствует. Остался только телефон с мобильным интернетом.
Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом все решения
и скрипты, которые у вас сейчас есть.

Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic
в файл scripts.txt, разделяя код строкой из 40 символов *. 

Пример содержимого файла scripts.txt:

import platform
import sys


info = 'OS info is {} Python version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
****************************************
print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("Введите вторую точку")
****************************************

…….
"""

import os

my_path = os.path.abspath(os.path.join(os.pardir, 'module_20_Python'))
print(my_path)
print(os.listdir(my_path))

for elem in os.listdir(my_path):
    new_path = os.path.join(my_path, elem)
    with open(new_path, 'r') as cur_file:
        data = cur_file.read()
        with open(os.path.join(os.curdir, 'scripts.txt'), 'a') as scripts_file:
            scripts_file.write(data)
            scripts_file.write('\n****************************************\n')


