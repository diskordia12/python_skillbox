"""
Задача 6. «Война и мир»
Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир».
Это довольно объёмное произведение лежит в архиве voina-i-mir.zip.
Напишите программу, которая подсчитывает статистику по буквам (не только русского алфавита)
в этом романе и выводит результат на экран (или в файл).
Результат должен быть отсортирован по частоте встречаемости букв
(по возрастанию или убыванию). Регистр символов имеет значение.

Архив можно распаковать вручную, но, если хотите,
можете изучить документацию по модулю zipfile (можно использовать и другой модуль)
и попробовать написать код, который будет распаковывать архив за вас.
"""

import zipfile
import os
import collections

file_name = 'voyna-i-mir.txt'

with zipfile.ZipFile('peace_and_war.zip', 'r') as zip_peace_and_war:
    zip_peace_and_war.extract(file_name)

all_letters = list()
frequency = collections.OrderedDict()

with open(os.path.join(os.curdir, file_name), 'r') as file:
    for line in file:
        for sym in line:
            if sym.isalpha():
                if sym not in frequency:
                    frequency[sym] = 0
                frequency[sym] += 1

frequency = dict(sorted(frequency.items(), key=lambda item: (-item[1], item[0])))
print(frequency)

for letter, freq in frequency.items():
    print(f'{letter} - {freq}')




