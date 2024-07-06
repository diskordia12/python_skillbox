"""
Задача 1. Таблица степеней
Аркадий как-то раз написал программу для вывода таблицы степеней для определённых чисел.
Недавно он узнал про такую штуку, как списки, и решил программу немного переписать,
а заодно усовершенствовать её.
По его задумке, вначале есть всего три числа: 3, 7 и 5,
а затем с помощью бесконечного цикла программа запрашивает новое число,
закидывает его в конец текущего списка чисел и выводит вторую, третью и четвёртую степень
каждого числа текущего списка. Вот какая программа получилась у Аркадия:

numbers = 3,7,5

while True:

 number = int(input('Новое число: '))

 numbers.append(numbers)

 print('Текущий список чисел:', numbers)

 for _ in number:

   print(i ** 2, i ** 3, i ** 4)

 print()

Пример верного результата:

> Новое число: 1
> Текущий список чисел: [3, 7, 5, 1]
> 9 27 81
> 49 343 2401
> 25 125 625
> 1 1 1

> Новое число: 2
> Текущий список чисел: [3, 7, 5, 1, 2]
> 9 27 81
> 49 343 2401
> 25 125 625
> 1 1 1
> 4 8 16


"""

# numbers = [3, 7, 5]
#
# while True:
#     number = int(input('Новое число: '))
#     numbers.append(number)
#     print(f'Текущий список чисел: {numbers}')
#
#     for i in numbers:
#         print(i ** 2, i ** 3, i ** 4)
#
#     print()

"""
Задача 2. Очень простая задача
У вас есть список numbers.
Напишите программу, которая заполняет список числами от 0 до 100 и выводит его на экран.
"""
# numbers = list()
#
# for n in range(100 + 1):
#     numbers.append(n)
#
# print(numbers)


"""
Задача 3. Контроль
В любой компании есть список сотрудников.
Руководство одной компании хочет знать, на рабочем месте ли сейчас сотрудник.
У каждого сотрудника есть пропуск со своим ID-номером (это положительное число),
список активных пропусков сотрудников известен заранее.

Напишите программу, которая сначала запрашивает у пользователя количество сотрудников в офисе,
ID их пропусков, а затем запрашивает ID пропуска, который нужно найти в этом списке.
Если такой есть, то вывести «Сотрудник на месте», а иначе «Сотрудник не работает!».

Пример:

Кол-во сотрудников в офисе: 4
> ID сотрудника: 10
> ID сотрудника: 20
> ID сотрудника: 30
> ID сотрудника: 40
> Какой ID ищем? 35
> Сотрудник не работает!
"""

# workers = int(input('Enter amount of workers in the office: '))
# workers_id = list()
#
# for _ in range(4):
#     id = int(input('Enter a worker id: '))
#     workers_id.append(id)
#
# desire_id = int(input('What id do you search: '))
#
# if desire_id in workers_id:
#     print('The worker is in the office.')
# else:
#     print('The worker doesn\'t work')


"""
Задача 1. Гугл
Программисты постоянно гуглят ошибки и ищут уже готовый код,
который можно использовать для своей программы, чтобы не изобретать велосипед.
Андрей поступил также и нашёл для своего проекта код,
который должен находить минимальное и максимальное числа в списке. Вот этот код:
"""

# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# maximum = nums_list[0]
# minimum = nums_list[0]
#
# for i in nums_list:
#     if maximum < i:
#         maximum = i
#
#     if minimum > i:
#         minimum = i
#
# print('Максимальное число в списке:', maximum)
#
# print('Минимальное число в списке:', minimum)

"""
Задача 2. Кратность
Пользователь вводит список из N чисел и число K.
Напишите код, выводящий на экран сумму индексов элементов списка, которые кратны K.

Пример:
> Кол-во чисел в списке: 4
> Введите 1 число: 1
> Введите 2 число: 20
> Введите 3 число: 30
> Введите 4 число: 4

> Введите делитель: 10

> Индекс числа 20: 1
> Индекс числа 30: 2

> Сумма индексов: 3
"""

# number_amount = int(input('Enter amount of numbers: '))
# numbers = list()
#
# for _ in range(number_amount):
#     num = int(input('Enter a number: '))
#     numbers.append(num)
#
# divider = int(input('Enter a divider: '))
# summ = 0

# for i_num in range(number_amount):
#     if numbers[i_num] % divider == 0:
#         summ += i_num
#         print(f'Index number {numbers[i_num]}: {i_num}')
#
# print(f'Sum of indexes: {summ}')


"""
Задача 3. Собачьи бега
В собачьих бегах участвует N собак,
у каждой из них есть определённое количество очков за сезон.
На огромном табло выводятся очки каждой собаки.
Однако при выводе был обнаружен баг:
собаки с наибольшим и наименьшим количеством очков поменялись местами! Нужно это исправить.

Дан список очков из N собак.
Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.
"""

# nums_list = []
# N = int(input('Amount of dogs: '))
#
# for _ in range(N):
#     num = int(input('Enter points of a dog: '))
#     nums_list.append(num)
#
# print(nums_list)
#
# maximum = nums_list[0]
# i_max = 0
# minimum = nums_list[0]
# i_min = 0
#
# for i_num in range(len(nums_list)):
#     if maximum < nums_list[i_num]:
#         maximum = nums_list[i_num]
#         i_max = i_num
#
#     if minimum > nums_list[i_num]:
#         minimum = nums_list[i_num]
#         i_min = i_num
#
# nums_list[i_max], nums_list[i_min] = nums_list[i_min], nums_list[i_max]
#
# print(nums_list)


"""
Задача 1. Текстовый редактор: возвращение
Мы продолжаем участвовать в разработке нового текстового редактора
 и делать жизнь обычных пользователей чуть лучше.
 В этот раз у нас стоит задача сделать фишку с поиском и заменой символов в выделенной строчке.
Например, человек что-то перечислял в тексте, но ошибся и вместо точек с запятой использовал
двоеточия. Лингвисты негодуют.

Пользователь вводит строку S.
Напишите программу, которая заменяет в строке все двоеточия (:) на точки с запятой (;).
Также подсчитайте количество замен и выведите ответ на экран (и новую строку тоже).
Для решения используйте список.

Пример:
> Введите строку: гвозди:шурупы:гайки
> Исправленная строка: гвозди;шурупы;гайки
> Кол-во замен: 2
"""
# My way
# user_text = input('Enter your text: ')
# user_text = user_text.replace(':', ';')
# count_sym = user_text.count(';')
# print(f'Remarked text: {user_text}\n'
#       f'Amount of replace: {count_sym}')

# The old way only with list

# user_text = input('Enter your text: ')
# user_text = list(user_text)
# count_sym = 0
# for i_sym in range(len(user_text)):
#     if user_text[i_sym] == ':':
#         user_text[i_sym] = ';'
#         count_sym += 1
# user_text = ''.join(user_text)
# print(f'Remarked text: {user_text}\n'
#       f'Amount of replace: {count_sym}')


"""
Задача 2. Соседи
Дана строка S и номер позиции символа в строке.
Напишите программу, которая выводит соседей этого символа
и сообщение о количестве таких же символов среди этих соседей:
их нет, есть ровно один или есть два таких же.

Пример 1:
> Введите строку: abbc
> Номер символа: 3

> Символ слева: b
> Символ справа: c
> Есть ровно один такой же символ.

Пример 2:
> Введите строку: abсd
> Номер символа: 3

> Символ слева: b
> Символ справа: d
> Таких же символов нет.
"""

# user_text = input('Enter yout text: ')
# symbol_number = int(input('Enter number of symbol: '))
# letters = list(user_text)
# left_symbol = letters[symbol_number - 1 - 1]
# right_symbol = letters[symbol_number - 1 + 1]

# count_same_symbols = 0
# if left_symbol == letters[symbol_number - 1]:
#     count_same_symbols += 1
#
# if right_symbol == letters[symbol_number - 1]:
#     count_same_symbols += 1
#
# print(f'Left symbol: {left_symbol}\n'
#       f'Right symbol: {right_symbol}')
# if count_same_symbols != 0:
#     print(f'Same symbols: {count_same_symbols}')
# else:
#     print('There are not same symbols')

"""
Задача 3. Улучшенная лингвистика
Мы уже писали программу для лингвистов,
которая считала количество определённых букв в тексте.
Теперь эту программу нужно улучшить.
Есть список из трёх слов, которые вводит пользователь.
Затем вводится сам текст произведения строго по словам.
Текст вводится до тех пор, пока не встретится слово end.
Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте.

Пример:
> Введите 1 слово: я
> Введите 2 слово: год
> Введите 3 слово: лучший

> Слово из текста: этот
> Слово из текста: год
> Слово из текста: -
> Слово из текста: лучший
> Слово из текста: год

> Подсчёт слов в тексте
> я: 0
> год: 2
> лучший: 1


"""

user_words = list()
user_text = ''
words_count = [0, 0, 0]

for i in range(3):
    word = input(f'Enter {i + 1} search word: ')
    user_words.append(word)

while True:
    user_text = input('Enter another word of your text: ')
    for i in range(3):
        if user_words[i] == user_text:
            words_count[i] += 1

    if user_text == 'end':
        break

print('Count words in text')
for i in range(3):
    print(f'{user_words[i]} : {words_count[i]}')