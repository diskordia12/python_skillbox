"""
Задача 1. Словарь квадратов чисел
На вход программе поступает целое число num.
Напишите программу создания словаря, который включает в себя ключи от 1 до num,
а значениями соответствующего ключа будет значение ключа в квадрате.

Пример:
Введите целое число: 5
Результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
import random

# initial_number = int(input('Enter a number: '))
# square_numbers = {number: number ** 2 for number in range(1, initial_number + 1)}
# print(f'Result: {square_numbers}')
# print(square_numbers[3])

"""
Задача 2. Студент
Пользователь вводит фамилию, имя студента, город проживания, вуз, в котором он учится,
и все его оценки. Всё вводится в одну строку через пробел.
Напишите программу, которая по этой информации составит словарь и выведет его на экран. 

Пример:
Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки):
Илья Иванов Москва МГУ 5 4 4 4 5

Результат: 
> Имя - Илья
> Фамилия - Иванов
> Город - Москва
> Место учёбы - МГУ
> Оценки - [5, 4, 4, 4, 5]
"""

# student_info = input('Enter info about a student with space (name, surname, city, study place, grades):\n')
# student_info = student_info.split()
# student_info_dict = dict()
# student_info_dict['name'] = student_info[0]
# student_info_dict['surname'] = student_info[1]
# student_info_dict['city'] = student_info[2]
# student_info_dict['study place'] = student_info[3]
# student_info_dict['grades'] = [int(grade) for grade in student_info[4:]]
#
# print('Result: ')
# for key in student_info_dict:
#     print(f'{key} - {student_info_dict[key]}')


"""
Задача 3. Контакты
Энтузиаст Степан, купив новый телефон, решил написать для него свою
собственную операционную систему. И, конечно же, первое, что он захотел в ней реализовать,
— это телефонная книга.
Напишите программу, которая запрашивает у пользователя имя контакта и номер телефона,
добавляет их в словарь и выводит на экран текущий словарь контактов.
Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы).
Обеспечьте контроль ввода: если это имя уже есть в словаре, то выведите соответствующее сообщение.

Пример:
> Текущие контакты на телефоне:
> <Пусто>
> Введите имя: Иван
> Введите номер телефона: 100200300 
> Текущие контакты на телефоне:
> Иван  100200300
> Введите имя: Лена
> Введите номер телефона: 8005555522 
> Текущие контакты на телефоне:
> Иван  100200300
> Лена  8005555522 
> Введите имя: Иван
> Ошибка: такое имя уже существует.
> ...
"""

# telephone_book = dict()
#
# while True:
#     if telephone_book:
#         print('\nTelephone book:')
#         for k, v in telephone_book.items():
#             print(f'{k} - {v}')
# else:
#     print('Telephone book is empty')
#
# name = input('\nEnter new name: ')
# if name in telephone_book:
#     print('Error. This name is already in a telephone book')
#     continue
#
# phone_number = input('Enter a phone number: ')
# telephone_book[name] = int(phone_number)


"""
Задача 1. Склады
У мебельного магазина есть два склада, на которых хранятся разные категории товаров по парам
«название — количество»:

small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}
big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
Магазин решил сократить аренду и скинуть все товары в большой склад (big_storage).
После этого нас попросили реализовать поиск по товарам.
Напишите программу, которая объединяет оба словаря в один (в big_storage),
затем запрашивает у пользователя название товара и выводит на экран его количество.
Если такого товара нет, то выводит об этом ошибку. Для получения значения используйте метод get.


"""

# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
#
# big_storage.update(small_storage)
#
# while True:
#     item = input('Enter an item: ')
#     print(f'{item}: {big_storage.get(item, "Not found")}')


"""
Задача 2. Кризис фруктов
Мы работаем в одной небольшой торговой компании, где все данные о продажах фруктов за год
сохранены в словаре в виде пар «название фрукта — доход»: 

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

В компании наступил небольшой кризис, и нам поручено провести небольшой анализ дохода.
Напишите программу, которая находит общий доход, затем выводит фрукт с минимальным доходом и 
удаляет его из словаря. Выведите итоговый словарь на экран.

Результат работы программы:
Общий доход за год составил 35419.34 рублей
Самый маленький доход у grapefruit. Он составляет 300.4 рублей
Итоговый словарь: {'apple': 5600.2, 'orange': 3500.45, 'banana': 5000.0, 'bergamot': 3700.56, 'durian': 5987.23, 'peach': 10000.5, 'pear': 1020.0, 'persimmon': 310.0}
"""

# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# year_income = sum(incomes.values())
# print(f'Year income: {year_income}')
# min_income = incomes['banana']
# fruit = ''
# for k,v in incomes.items():
#     if min_income > v:
#         min_income = v
#         fruit = k
# print(f'Fruit with min income: {fruit} - {min_income}')
# incomes.pop(fruit)
# print(incomes)

# # Their way
# def get_value(x):
#     return x[1]
#
#
# min_name, min_value = min(incomes.items(), key=get_value)
# # При помощи функции и параметра key мы говорим пайтону как именно надо сравнивать между собой элементы
# # Т.к. элементы записаны в таком виде - ('apple': 5600.20), а сравнивать мы хотим по значениям - то нам проосто надо брать для сравнения
# # элементы под индексом 1 (если бы сравнивали по ключам, то индекс надо было бы заменить на 0)
# print(result_sum, min_name, min_value)

"""
Задача 3. Гистограмма частоты
Лингвистам нужно собрать данные о частоте букв в тексте, исходя из этих данных будет строиться
гистограмма частоты букв. 
Напишите программу, которая получает сам текст и считает,
сколько раз в строке встречается каждый символ.
На экран нужно вывести содержимое в виде таблицы, отсортированное по алфавиту,
а также максимальное значение частоты.

Пример:
Введите текст: Здесь что-то написано
  : 2
- : 1
З : 1
а : 2
д : 1
е : 1
и : 1
н : 2
о : 3
п : 1
с : 2
т : 2
ч : 1
ь : 1
Максимальная частота: 3
"""

# def get_frequency(text: str) -> dict:
#     frequency = dict()
#     for sym in text:
#         if sym in frequency:
#             frequency[sym] += 1
#         else:
#             frequency[sym] = 1
#     return frequency
#
#
# user_text = input('Enter your text: ')
# sym_frequency = get_frequency(user_text)
# print(f'Frequency: ')
# for sym, freq in sorted(sym_frequency.items()):
#     print(f'{sym}: {freq}')


"""
Задача 1. Заказ фруктов
В торговую компанию пришёл заказ:
order = {'apple': 2,
         'banana': 3,
         'pear': 1,
         'watermelon': 10,
         'chocolate': 5}

Ключи — названия товаров, значения — необходимое количество килограммов.
При помощи метода get и установки значения по умолчанию проверьте, есть ли товар на складе,
и получите его цену. Если товара нет, то по умолчанию получите 0.
Подсчитайте итоговую выручку компании по имеющимся товарам.
incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

Ключи — названия товаров, значения — цена за один килограмм.
Напишите программу, которая суммирует стоимость (цена × количество) всех заказанных товаров,
и выведите итоговую сумму в консоль.
Если искомого товара нет на складе, то по умолчанию получите 0.
В этом поможет метод get и установка значения по умолчанию.


"""

# order = {'apple': 2,
#          'banana': 3,
#          'pear': 1,
#          'watermelon': 10,
#          'chocolate': 5}
#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# order_info = {fruit: incomes.get(fruit, 0) for fruit in order}
# print(order_info)
#
# earnings = sum([order_info[fruit] * order[fruit] for fruit in order])
# print(f'Company earnings: {earnings}')
#
# result_sum = 0
# for fruit_name in order:
#     cost = incomes.get(fruit_name, 0) * order[fruit_name]
#     result_sum += cost
#
# print("Итоговая стоимость товаров из заказа составляет:", result_sum)


"""
Задача 2. Игроки
Есть готовый словарь игроков, у каждого игрока есть имя, команда,
в которой он играет, а также его текущий статус, в котором указано, отдыхает он,
тренируется или путешествует:

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
} 

Напишите программу, которая выводит на экран следующие данные в разных строках:
Все члены команды А, которые отдыхают.
Все члены команды B, которые тренируются.
Все члены команды C, которые путешествуют.
"""
#
# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# team_a_players = [player['name']
#                   for player in players_dict.values()
#                   if player['team'] == 'A' and player['status'] == 'Rest'
#                   ]
# print(f'Все члены команды А, которые отдыхают: {team_a_players}')
#
# team_b_players = [player['name']
#                   for player in players_dict.values()
#                   if player['team'] == 'B' and player['status'] == 'Training'
#                   ]
# print(f'Все члены команды B, которые тренируются: {team_b_players}')
#
#
# team_c_players = [player['name']
#                   for player in players_dict.values()
#                   if player['team'] == 'C' and player['status'] == 'Travel'
#                   ]
# print(f'Все члены команды C, которые путешествуют: {team_c_players}')

# # Their way
# # Чтобы не прописывать решение "в лоб", вручную подставляя статус и команду - попробуем сформировать дополнительные словарь и список,
# # чтобы автоматизировать этот процесс:
# help_dict = {"Rest": "отдыхают",
#              "Training": "тренируются",
#              "Travel": "путешествуют"}
#
# team_order = ["A", "B", "C"]
#
# # Запустим цикл по словарю состояний и одновременно будем вести счёт состояний, чтобы на каждой итерации выбирать одну из команд:
# index = 0
# for state in help_dict:
#     print(f"Все члены команды из команды {team_order[index]}, которые {help_dict[state]}:")
#     for _, player in players_dict.items():
#         if player["status"] == state and player["team"] == team_order[index]:
#             print(player["name"])
#     index += 1


"""
Задача 1. Пунктуация
Напишите программу, которая считает количество знаков пунктуации в символьной строке.
К знакам пунктуации относятся символы из набора ".,;:!?". Набор должен храниться в виде множества.

Пример:
Введите строку: Я! Есть. Грут?! Я, Грут и Есть.
Количество знаков пунктуации: 4
"""

# punctuation = set()
# punctuation.update([',', ';', ':', '!', '?'])
#
# message = input('Your message: ')
# amount_punct = 0
#
# for sym in message:
#     if sym in punctuation:
#         amount_punct += 1
#
# print(f'Number of punctuation marks: {amount_punct}')

"""
Задача 2. Семинар
На одном семинаре по теории множеств нужно показать наглядный пример,
как эти множества работают. Для начала было сгенерировано два набора чисел: 

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

Вас попросили написать программу, которая будет наглядно демонстрировать работу со множествами
с помощью этих чисел.
Напишите программу, которая преобразует списки во множества и убирает повторяющиеся элементы.
Затем удаляет минимальный элемент из каждого множества и добавляет туда случайное число
в диапазоне от 100 до 200. Затем выполните следующие действия со множествами: 

- Вывести все элементы множеств (объединение). 
- Вывести только общие элементы (пересечение).
- Вывести элементы, входящие в nums_2, но не входящие в nums_1.
 
Пример результата:
1-е множество: {1, 2, 3, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 24, 26, 27, 29}
2-е множество: {1, 5, 7, 8, 9, 11, 12, 13, 15, 16, 19, 21, 22, 23, 24, 29, 30}
 
Минимальный элемент 1-го множества: 1
Минимальный элемент 2-го множества: 1
 
Случайное число для 1-го множества: 126
Случайное число для 2-го множества: 169

Объединение множеств: {2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 29, 30, 169, 126}
Пересечение множеств: {7, 8, 11, 12, 13, 15, 16, 19, 21, 22, 24, 29}
Элементы, входящие в nums_2, но не входящие в nums_1: {5, 9, 169, 23, 30}
"""

# nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
#
# nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
#
# nums_1 = set(nums_1)
# nums_2 = set(nums_2)
# print(f'The first set: {nums_1}')
# print(f'The second set: {nums_2}')
#
# min_nums_1 = min(nums_1)
# min_nums_2 = min(nums_2)
# print(f'Min elem of first set: {min_nums_1}')
# print(f'Min elem of second set: {min_nums_2}')
#
# nums_1.remove(min_nums_1)
# nums_2.remove(min_nums_2)
#
# random_nums_1 = random.randint(100, 200)
# random_nums_2 = random.randint(100, 200)
# print(f'Random number for the first set: {random_nums_1}')
# print(f'Random number for the second set: {random_nums_2}')
#
# nums_1.add(random_nums_1)
# nums_2.add(random_nums_2)
#
# print(f'Union of sets: {nums_1.union(nums_2)}')
# print(f'Intersections of sets: {nums_1.intersection(nums_2)}')
# print(f'Intersections of sets: {nums_2.difference(nums_1)}')



"""
Задача 3. Различные цифры
Напишите программу, которая находит все различные цифры в символьной строке.
Для решения используйте множество
(цифры будут различные, и поиск во множестве намного быстрее, чем в списке).
Подсказка: можно использовать вот такое сравнение '0'<=x<='9'

Пример:
Введите строку: ab1n32kz2
Различные цифры строки: 123
"""

message = set(input('Enter message: '))

digits = set()

for sym in message:
    if sym.isdigit():
        digits.add(sym)

print(f'Different digits: {"".join(digits)}')


# Another way

text = input("Введите строку: ")
text_unique = set(text)
result = text_unique & set("0123456789")
# При помощи множества выделим из строки только общие элементы (цифры) и посчитаем длину множества
print(''.join(result))

# Решение через цикл и сравнение:
new_result = set()
for symbol in text:
    if '0' <= symbol <= '9':
        new_result.add(symbol)

print(''.join(new_result))
