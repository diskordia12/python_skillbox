"""
Задание 3. Файлы
В IT-компании есть негласные правила именования текстовых документов:
- Название файла не может начинаться с одного из специальных символов: @, №, $, %, ^, &, *, ().
- Файл должен заканчиваться расширением .txt или .docx.
Напишите программу, которая получает на вход полное название файла и проверяет,
соответствует ли он этим правилам.

Пример 1
Название файла: @example.txt.
Ошибка: название начинается недопустимым символом.

Пример 2
Название файла: example.ttx.
Ошибка: неверное расширение файла. Ожидалось .txt или .docx.

Пример 3
Название файла: example.txt.
Файл назван верно.
"""

file_name = input('Enter a file name: ')

prohibited_sym = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
extension = ('.txt', '.docx')

if file_name.startswith(prohibited_sym):
    print('Error. Name starts with prohibited symbol')
elif not file_name.endswith(extension):
    print('Error. Wrong file extension')
else:
    print('File name is correct')

