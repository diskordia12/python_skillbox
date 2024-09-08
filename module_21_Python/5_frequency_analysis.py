"""
Задача 5. Частотный анализ
Есть файл text.txt, который содержит текст.
Напишите программу, которая выполняет частотный анализ,
определяя долю каждой буквы английского алфавита в общем количестве английских букв в тексте,
и выводит результат в файл analysis.txt.
Символы, не являющиеся буквами английского алфавита, учитывать не нужно.

В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте,
с тремя знаками в дробной части.
Буквы должны быть отсортированы по убыванию их доли.
Буквы с равной долей должны следовать в алфавитном порядке.

Пример:
Содержимое файла text.txt:
Mama myla ramu.

Содержимое файла analysis.txt:
a 0.333
m 0.333
l 0.083
r 0.083
u 0.083
y 0.083
"""

import os

# data = list()
letters = dict()
frequency = dict()

with open(os.path.join(os.curdir, 'text.txt'), 'r') as text_file:
    for line in text_file:
        for sym in line:
            if sym.isalpha():
                if sym in letters:
                    letters[sym.lower()] += 1
                else:
                    letters[sym.lower()] = 1

amount_of_letters = sum(letters.values())


for letter, letter_count in letters.items():
    frequency[letter] = round(letter_count / amount_of_letters, 3)

print(letters)
print(frequency)
# Sort dict with lambda (take pair key and value) function.
# First reverse sort by values of dict (-item[1])
# then sort by keys(letters) (item[0]).
# Letters with equal keyes should follow alphabetical order
frequency = dict(sorted(frequency.items(), key=lambda item: (-item[1], item[0])))
print(frequency)

with open(os.path.join(os.curdir, 'analysis.txt'), 'w') as analysis_file:
    for symbol, frequency in frequency.items():
        analysis_file.write(f'{frequency:.3f} {symbol}\n')

