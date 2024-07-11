# """
# Задача 1. Заказ
# После того, как человек сделал заказ в интернет-магазине, ему на почту приходит оповещение
# с его именем и номером заказа.
# Напишите программу, которая получает на вход имя и код заказа,
# а затем выводит на экран соответствующее сообщение.
# Для решения используйте строковый метод format.
#
# Пример:
# > Имя: Иван
# > Номер заказа: 10948
# > Здравствуйте, Иван! Ваш номер заказа: 10948. Приятного дня!
# """
#
# # user_name = input('Your name: ')
# # order_number = input('Order number: ')
# # message = 'Hello, {name}! Your order number: {number}. Have a nice day!'.format(
# #             name=user_name,
# #             number=order_number)
# # print(message)
#
# """
# Задача 2. Долги
# Один наш друг занял у нас определённую сумму денег и всё никак не может их вернуть.
# А деньги нам нужны. Поэтому мы решили написать небольшой скрипт-напоминалку,
# который, возможно, разбудит его совесть.
# Напишите программу, которая получает на вход имя и долг,
# а затем выводит на экран сообщение, где имя повторяется несколько раз (и долг, возможно, тоже).
# Используйте числа в названиях ключей.
#
# Пример:
# > Введите имя: Том
# > Введите долг: 100
# > Том! Том, привет! Как дела, Том? Где мои 100 рублей? Том!
# """
# # name = input('Name: ')
# # loan = input(f'How much many {name} own to you: ')
# # message = '{0}! {0}, hello! How are you, {0}? Where is my {1} euros? {0}!'.format(name, loan)
# # print(message)
#
# """
# Задача 3. IP-адрес
# IP-адрес компьютера состоит из 4 чисел, разделённых точкой.
# Каждое число находится в диапазоне от 0 до 255 (включительно).
#
# Пример правильного адреса: 192.168.1.0
# Пример неправильного адреса: 192.168.300.0
# Напишите программу, которая получает на вход 4 числа и выводит на экран IP-адрес.
# Используйте переменную ip_address в качестве шаблона. Обеспечьте контроль ввода.
# """
#
# # ip_address = '{0}.{1}.{2}.{3}'
# # numbers = list()
# # count = 0
# # while count < 4:
# #     num = int(input('Enter part of ip: '))
# #     if num > 255 or num < 0:
# #         print('Wrong num. Only from 0 to 255')
# #         continue
# #
# #     count += 1
# #     numbers.append(num)
# #
# # print(ip_address.format(*numbers))
# # # * полезный инструмент, но и без него можно справиться, вручную прописав элементы по индексам
# # print(ip_address.format(numbers[0], numbers[1], numbers[2], numbers[3]))
#
# """
# Задача 1. Улучшенная лингвистика 2
# Усовершенствуйте старую программу:
# У нас есть список из трёх слов, которые вводит пользователь.
# Затем вводится сам текст произведения, который вводится уже в одну строку.
# Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте.
# """
# # key_words = input('Enter words for search: ').split()
# # message = input('Your text: ').split()
# # key_count = [message.count(word) for word in key_words]
# #
# # result = [': '.join([key_words[i], str(key_count[i])])
# #             for i in range(3)]
# # result = ' '.join(result)
# # print(result)
#
# """
# Задача 2. Бабушка
# У одной бабушки, когда та переписывается с внуком, постоянно залипает кнопка пробела.
# В итоге между словами получаются огромные расстояния.
# Внук не знает как это поправить в самом телефоне, поэтому обратился к вам за помощью.
# Пользователь вводит строку. Напишите программу, которая преобразовывает в этой строке
# все идущие подряд пробелы в один и выводит результат на экран.
#
# Пример:
# Введите текст: У       нас         пошёл                    снег    !
# Исправленный текст: У нас пошёл снег !
# """
# # message = input('Your message: ').split()
# # correct_message = ' '.join(message)
# # print(f'Correct message: {correct_message}')
#
# """
# Задача 3. Разделители символов
# Человек хочет сделать рассылку поздравлений для определённого списка людей.
# Поздравления для разных людей он хочет написать по-разному.
# Напишите программу, которая запрашивает у пользователя:
# Шаблон поздравления (туда вставляется ФИ и возраст)
# ФИ людей (в одну строку, разделяются запятой)
# Возраст каждого человека (в одну строку через пробел)
# В конце  программа выводит поздравления и всех именинников в одну строку вместе с их возрастом.
#
# Пример:
# > Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}:
# > С днём рождения, {name}! С {age}-летием тебя!
# > Список людей через запятую: Иван Иванов, Петя Петров, Лена Ленова
# > Возраст людей через пробел: 20 30 18
#
# > С днём рождения, Иван Иванов! С 20-летием тебя!
# > С днём рождения, Петя Петров! С 30-летием тебя!
# > С днём рождения, Лена Ленова! С 18-летием тебя!
# > Именинники: Иван Иванов 20, Петя Петров 30, Лена Ленова 18
# # """
# # while True:
# #     sample_message = input('Enter sample message, use {name} and {age}: ')
# #     if '{name}' in sample_message and '{age}' in sample_message:
# #         break
# #     print('Error. Add {name} and {age}')
# #
# # people = input('People: ').split(', ')
# # ages = input('Ages: ').split()
# # ages = [int(age) for age in ages]
# #
# # for i_man in range(len(people)):
# #     print(sample_message.format(name=people[i_man], age=ages[i_man]))
# #
# # merge_people = [' '.join([people[i_man], str(ages[i_man])])
# #                 for i_man in range(len(people))]
# # merge_people = ', '.join(merge_people)
# # print(f'All birthday people: {merge_people}')
#
#
# """
# Задача 1. Шифр Цезаря 2
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря.
# Напомним, что в таком способе шифрования каждая буква заменяется на следующую по алфавиту через K
# позиций по кругу.
# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования.
# Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре.
# """
# # My way
# # alphabet = [chr(ord('A') + alphabetIndex) for alphabetIndex in range(0, 26)]
# # print(alphabet)
# # user_message = input('Say something: ')
# # shift = int(input('Shift: '))
# #
# # user_message = user_message.upper().split(' ')
# #
# # cipher_message = [[alphabet[(alphabet.index(letter) + shift) % 26] for letter in word]
# #                    for word in user_message]
# #
# # print('Cipher message: ', end='')
# # for word in cipher_message:
# #     for letter in word:
# #         print(letter, end='')
# #     print(end=' ')
#
# # Their way
# # print(ord("а"), ord("я"), ord("ё"), chr(1104))
# #
# # text = input("Введите текст: ")
# # delta = int(input("Введите сдвиг: "))
# # alphabet = [chr(index) for index in range(ord("а"), ord("я") + 1)]  # заполняем список буквами алфавита
# # # Думаем над структурой алгоритма: [вариант_1 если условие_1 иначе вариант_2 for буква in текст]
# # new_text = [alphabet[(alphabet.index(letter) + delta) % len(alphabet)] if letter in alphabet else letter for letter in text.lower()]
# # print(''.join(new_text))
#
# """
# Задача 2. Путь к файлу
# Все данные сайта лежат в одном проекте. При написании кода, внутри этого проекта
# часто используются абсолютные пути файлов, которые необходимо проверять.
# Пользователь вводит абсолютный путь к текстовому файлу,
# а также проверяемые данные: диск и расширение файла.
# Напишите программу, которая проверяет корректность этого пути.
#
# Пример:
# > Путь к файлу: C:/user/docs/folder/new_file.txt
# > На каком диске должен лежать файл: C
# > Требуемое расширение файла: .txt
# > Путь корректен!
# """
#
# # path = input('Enter a path: ')
# # disc = input('Which disc: ')
# # file_extension = input('file extension: ')
# #
# # if not path.startswith(disc):
# #     print('Wrong disc')
# # elif not path.endswith(file_extension):
# #     print('Wrong extension')
# # else:
# #     print('Path is right')
#
# """
# Задача 3. Удаление части
# На вход в программу подаётся строка, состоящая из прописных и заглавных букв кириллицы.
# Напишите код, который проверяет, каких букв в строке больше, прописных или заглавных.
# Если заглавных букв больше, то сделать все буквы строки заглавными, иначе сделать все прописными.
# Подсказка: используйте методы islower() и/или isupper().
#
# Пример:
# > Введите строку: ПитоН - этО хорошО
# > Результат: питон - это хорошо
# Пример 2:
# > Введите строку: ПиТоН - ЭтО УДоБнО
# > Результат: ПИТОН - ЭТО УДОБНО
# """
# message = input('Enter your message: ')
# lowers = len([letter for letter in message if letter.islower()])
# uppers = len([letter for letter in message if letter.isupper()])
#
# # count_lower = 0
# # count_upper = 0
# # for letter in message:
# #     if letter.islower():
# #         count_lower += 1
# #     else:
# #         count_upper += 1
#
# if lowers > uppers:
#     print(message.lower())
# else:
#     print(message.upper())

from math import pi

print('PI equals to {:.5f}'.format(pi))
print(f'PI equals to {pi:.5f}')
