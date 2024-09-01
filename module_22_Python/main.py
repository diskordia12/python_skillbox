"""
Задача 1. Пятый элемент
В курсе по программированию студенту дали простую задачу:
умножить константу (число 42) на пятый элемент строки, введённой пользователем. Вот код студента:

BRUCE_WILLIS = 42
input_data = input('Введите строку: ')
leeloo = int(input_data[4])
result = BRUCE_WILLIS * leeloo
print(f'- Leeloo Dallas! Multi-pass № {result}!')

Модифицируйте этот код, обработав исключения для произвольных входных параметров:
ValueError — невозможно преобразовать к числу,
IndexError — выход за границы списка,
остальные исключения.
Для каждого типа исключений выведите на консоль соответствующее сообщение.
"""
#
# BRUCE_WILLIS = 42
# input_data = input('Введите строку: ')
# try:
#     leeloo = int(input_data[4])
#     result = BRUCE_WILLIS * leeloo
#     print(f'- Leeloo Dallas! Multi-pass № {result}!')
# except ValueError as e:
#     print(f'{e} - невозможно преобразовать к числу')
# except IndexError as e:
#     print(f'{e} - выход за границы списка')
# except Exception:
#     print('Something went wrong')

"""
Задача 2. Возраст
Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.

Напишите программу, которая считывает файл, даёт имя для каждого возраста
(можно просто использовать буквы алфавита) и выводит результат в новый файл result.txt
в формате «имя — возраст». Программа должна обрабатывать следующие ошибки и
выводить сообщение на экран:
- Попытка создания файла, который уже существует.
- На чтение ожидался файл, но это оказалась директория.
- Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
"""

# import os
#
# names = [name for name in 'abcdefghjk']
# ages = list()
#
# try:
#     with open('ages.txt', 'r') as file_ages:
#         for line in file_ages:
#             ages.append(line)
# except IsADirectoryError as e:
#     print(f'{e} - На чтение ожидался файл, но это оказалась директория')
# except ValueError as e:
#     print(f'{e} - Неверный тип данных и некорректное значение')
#
# names_and_ages = [name_age for name_age in zip(names, ages)]
# print(names_and_ages)
#
# try:
#     with open('result.txt', 'x') as file_result:
#         for person in names_and_ages:
#             file_result.write(' '.join(person))
# except FileExistsError as e:
#     print(f'{e} - Попытка создания файла, который уже существует')
#




# # Their solution
#
# file_ages = None
# file_result = None
#
# try:
#     file_ages = open("ages.txt", "r", encoding="utf8")
#     file_result = open("result.txt", "x", encoding="utf8")
#     # режим 'x' - это эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
# except (FileExistsError, PermissionError, IsADirectoryError) as exc:  # названия исключений можно группировать в кортежи
#     print("Поймано исключение: ", exc, type(exc))
#
# if file_result and file_ages:
#     names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#     count = 0
#     for line in file_ages:
#         try:
#             clear_line = line.rstrip()
#             int(clear_line)  # на всякий случай пытаемся преобразить данные в int, но не сохраняем это в переменную, т.к. записывать нам
#             # в файл придётся именно строку
#             file_result.write(names[count] + " - " + clear_line)
#             count += 1
#         except (ValueError, TypeError) as exc:
#             print("Поймано исключение: ", exc, type(exc))
#
#     file_ages.close()
#     file_result.close()

"""
Задача 1. Простая программа
Напишите программу, которая открывает файл и записывает туда введённую пользователем строку.
Используйте операторы try except else finally. Обработайте возможные ошибки:

Проблема при открытии файла.
Нельзя преобразовать данные в целое.
Неожиданная ошибка.
"""

import os
#
# try:
#     file_test = open('for_test.txt', 'w')
#
#     user_message = int(input('Enter you message: '))
#     file_test.write(str(user_message))
#
# except (FileNotFoundError, PermissionError) as exc:
#     print(type(exc), exc)
# except ValueError as exc:
#     print(type(exc), exc)
# except Exception as exc:
#     print(type(exc), exc)
# else:
#     print('Successfully done')
# finally:
#     file_test.close()
#     print(file_test.closed)


"""
Задача 2. Старая задача
Возьмите любую задачу из домашнего задания, например, предыдущего модуля и
оформите её решение в виде try except finally (можно ещё и else), обрабатывая возможные ошибки.
Посмотрев на то, что получилось, попробуйте ответить себе на такой вопрос:
когда стоит использовать обработку исключений и когда она будет излишней?
# """
#
# def find_file(cur_path, file_name):
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
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
#
# try:
#     find_file('c:\\', 'hel')
# except (TypeError, PermissionError) as exc:
#     print(exc, type(exc))

"""
Хоть проверка исключений и является мощным инструментом,
НО отдавать предпочтение нужно простым проверкам (избежать исключения лучше)
Если же мы не уверены в появлении ошибки (например у нас нет власти над источником ошибки
- это может быть какой-то сторонний сервис)
И если простая проверка не поможет учесть все варианты - мы можем использовать исключения.
НО даже в этом случае, старайтесь разделять исключения,
которые вы выбрасываете специально и исключения которые могут появиться случайно.
Причина такой осторожности в том, что мы можем запутаться и поймать например исключение,
о котором мы не догадывались. А если мы его
поймаем и не увидим - мы можем пропустить ошибку в нашем коде.
"""

"""
Задача 1. Имена
В базе данных одной компании есть баг (или, может быть, фича):
если ввести туда имя сотрудника меньше чем из трёх букв,
то база сломается и упадёт. Как компания принимает на работу людей, например,
с китайскими именами, непонятно.

Дан файл people.txt, в котором построчно хранится N имён пользователей. 
Напишите программу, которая берёт количество символов в каждой строке файла и в
качестве ответа выводит общую сумму.
Если в какой-либо строке меньше трёх символов (не считая литерала \n),
то вызывается ошибка, и программа завершается.

Содержимое файла people.txt:
Петя
Ян
Маша
Ева
Дмитрий
Анастасия
"""

# sum_of_name_char = 0
#
# with open('people.txt', 'r') as file_people:
#     for name in file_people:
#         if len(name.strip()) < 3:
#             raise ValueError(f'Length of name {name.strip()} less than 3 chars')
#         sum_of_name_char += len(name.strip())
#
# print(sum_of_name_char)


"""
Задача 2. Логирование
Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются,
но и записывают эту ошибку в файл.
Таким образом проще сформировать отчёт об ошибках, а значит, программисту будет проще их исправить.
Это называется логированием ошибок.

Дан файл words.txt, в котором построчно записаны слова.
Необходимо определить количество слов, из которых можно получить палиндром
(привет предыдущим модулям).
Если в строке встречается число, то программа выдаёт ошибку ValueError и
записывает эту ошибку в файл errors.log
"""


def check_palindrome(word: str) -> bool:
    control_set = set()
    for symbol in word:
        if symbol in control_set:
            control_set.remove(symbol)
        else:
            control_set.add(symbol)

    if len(control_set) <= 1:
        return True
    else:
        return False


amount_of_palindromes = 0


with open('words.txt', 'r') as file_words:
    for word in file_words:
        try:
            clear_word = word.strip()
            if clear_word.isalpha():
                if check_palindrome(clear_word):
                    amount_of_palindromes += 1
            else:
                raise ValueError(f'The string {clear_word} is not completely composed of letters!')
        except ValueError as e:
            with open('errors.log', 'a') as errors_log:
                errors_log.write(str(e))
                errors_log.write('\n')

print(f'Amount words witch can be convert to a palindrome: {amount_of_palindromes}')

