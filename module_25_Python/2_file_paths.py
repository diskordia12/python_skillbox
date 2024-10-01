"""
Задача 2. Пути файлов
Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам
(включая вложенные папки и подпапки) указанной директории
(по умолчанию — корневой диск), находит указанный пользователем каталог
и генерирует пути всех встреченных файлов.

Подсказка: вместо написания кода с рекурсией используйте
готовую рекурсивную функцию os.walk():
os — Miscellaneous operating system interfaces — Python 3.11.0 documentation.
"""

import os


def gen_files_path(search_directory: str, start_directory=os.path.abspath(os.sep)) -> str:
    for address, dirs, files in os.walk(start_directory, topdown=True):
        if search_directory in dirs:
            print(f'Found: {os.path.join(address, search_directory)}')
            return
        for name in files:
            yield os.path.join(address, name)


my_path = os.path.abspath(os.path.join(os.pardir, os.pardir, 'python_skillbox'))

for file in gen_files_path('task', my_path):
    print(file)


