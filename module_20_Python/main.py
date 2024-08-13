"""
Задача 1. Challenge
Обычно программисты любят, когда всё просто и понятно.
Но Антон не из таких. Он любит устраивать себе челлендж,
развиваться и сразу применять на практике то, что только что узнал.
И в этот раз он подумал реализовать подсчёт факториала без использования циклов.
Напишите функцию, которая считает факториал числа с помощью рекурсии.
Кстати, в Python есть ограничение на количество рекурсивных вызовов.
Попробуйте передать своей функции, например, число 1000 и посмотрите, что будет.
"""

# def factorial(num: int) -> int:
#     if num == 1:
#         return num
#     return num * factorial(num - 1)
#
#
# print(factorial(3))
# print(factorial(5))


"""
Задача 2. Степень числа
На одном из форумов, посвящённых программированию,
пользователь выложил такой код для расчёта степени числа без использования циклов,
** и функции math.pow():

def power(a, n):
    return a * power(a, n)
 
float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))
print(float_num, '**', int_num, '=', power(float_num, int_num))
 
Другие пользователи отметили, что это решение нерабочее и в нём есть ошибки.
Исправьте это решение, не используя циклы, возведение в степень через ** и функцию math.pow()

Правильный результат:
> Введите вещественное число: 1.5
> Введите степень числа: 5
> 1.5 ** 5 = 7.59375

2**3 = 2 * 2**2
2**2 = 2 ** 2**1
"""

# def power(a, n):
#     if n == 1:
#         return a
#     return a * power(a, n - 1)
#
#
# user_num = float(input('Введите вещественное число: '))
# power_of_num = int(input('Введите степень числа: '))
# print(f'{user_num} ** {power_of_num} = {power(user_num, power_of_num)} ')

"""
Задача 3. Поиск элемента
Когда мы работаем с большой многоуровневой структурой, нам нередко необходимо пройтись по ней
и найти нужный элемент. Для этого в программировании используются специальные алгоритмы поиска.
Напишите функцию, которая находит заданный пользователем ключ в словаре
и выдаёт значение этого ключа на экран. В качестве примера можно использовать такой словарь:

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

Пример 1:
Искомый ключ: h2
Значение: Здесь будет мой заголовок

Пример 2:
Искомый ключ: abc
Такого ключа в структуре сайта нет.
"""
#
#
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
#
# def search_element(struct: dict, key: str) -> str:
#     result = None
#     if key in struct:
#         return struct[key]
#
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             result = search_element(sub_struct, key)
#             if result:
#                 return result
#
#     return result
#
#
# user_key = input('Enter a key for search: ')
# value = search_element(site, user_key)
# if value:
#     print(f'Result: {value}')
# else:
#     print('There are not such a key')


"""
Задача 1. Ошибка
В одном проекте на 10 000 строк кода произошла критическая ошибка.
Хорошо, что старший разработчик быстро её нашёл и исправил.
Он решил проверить, смогли бы вы её исправить, если бы его не было на месте.
Поэтому он написал для вас код с аналогичной ошибкой:

import random
 
def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)
 
 
nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
 
change_dict(common_dict)
print(common_dict)
 

Суть кода в том, что у вас есть общий словарь из нескольких ключей,
значения которых равны ранее объявленным переменным.
Затем вызывается функция, которая должна изменять значения словаря,
добавляя к значениям случайное число, в зависимости от типа данных.
Но при этом меняются и ранее объявленные переменные.
Исправьте эту ошибку и убедитесь, что nums_list, some_dict и uniq_nums не меняются.

Подсказка. Для копирования объектов есть несколько способов:

Встроенный метод copy. Пример для словаря.
Встроенный в Python модуль copy и функции copy.copy() и copy.deepcopy().
"""
#
# import random
# import copy
#
#
# def change_dict(dct: dict):
#     num = random.randint(1, 100)
#     for i_key, i_value in dct.items():
#         if isinstance(i_value, list):
#             i_value.append(num)
#         if isinstance(i_value, dict):
#             i_value[num] = i_key
#         if isinstance(i_value, set):
#             i_value.add(num)
#
#
# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
# common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
# common_dict_copy = copy.deepcopy(common_dict)
#
# change_dict(common_dict_copy)
# print(common_dict_copy)
# print(f'nums list: {nums_list}')
# print(f'some dict: {some_dict}')
# print(f'uniq nums: {uniq_nums}')


"""
Задача 2. Непонятно!
Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками,
объектами и их id. Видя, как он мучается, вы решили помочь ему и объяснить эту тему наглядно.
Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных,
информацию о его изменяемости, а также id этого объекта.

Помните, что через input можно получить только строку,
что бы вы ни вводили.
В данном случае ввод можно выполнить вручную, просто вписав нужный объект в переменную,
без использования функции input.

Пример 1:
Введите данные: привет
Тип данных: str (строка)
Неизменяемый (immutable)
Id объекта: 1705156583984

Пример 2:
Введите данные: {‘a’: 10, ‘b’: 20}
Тип данных: dict (словарь)
Изменяемый (mutable)
Id объекта: 1705205308536
"""
#
# my_text = 'geralt'
# my_number = 34
# my_list = [1, 2, 3]
# my_dict = {1: 'no', 2: 'yes'}
# my_set = {2, 4, 5}
# my_tuple = (2, 1, 4)
#
#
# data_names_dict = {
#     "<class 'str'>": "строка",
#     "<class 'dict'>": "словарь",
#     "<class 'list'>": "список",
#     "<class 'set'>": "множество"
# }
#
# mutable_check_helper = {
#     "mutable": ("словарь", "список", "множество")
# }
#
#
# def check_info(data):
#     type_of_data = type(data)
#     name_of_data = ""
#     if str(type_of_data) in data_names_dict:
#         name_of_data = data_names_dict[str(type_of_data)]
#
#     if name_of_data in mutable_check_helper["mutable"]:
#         property_of_data = "Изменяемый (mutable)"
#     else:
#         property_of_data = "Неизменяемый (immutable)"
#
#     print(f"Тип данных: {type_of_data} ({name_of_data})")
#     print(property_of_data)
#     print("Id объекта:", id(data))
#
#
# data_in = "привет"
# check_info(data_in)
#
# check_info(my_number)


"""
Задача 1. Работа с файлом
Вы пишете небольшое приложение для работы с файлами.
Реализуйте функцию, которая может принимать на вход три аргумента:
вопрос пользователю (на который нужно ответить да или нет),
сообщение о неправильном вводе и количество попыток.
Вопрос — обязательный позиционный аргумент, остальные — со значениями по умолчанию.
При корректном ответе функция может возвращать что угодно — например,
число 1 при ответе «да» или 0 при ответе «нет».
В основной программе вызовите функцию минимум три раза: только с вопросом, с вопросом и сообщением
об ошибке, с вопросом и количеством попыток.

Пример работы программы:
Вы действительно хотите выйти? что
Неверный ввод. Пожалуйста, введите 'да' или 'нет'.
Осталось попыток: 3
Вы действительно хотите выйти? да

Удалить файл? не знаю
Так удалить или нет? 
Осталось попыток: 3

Удалить файл? нет

Записать файл? ага
Неверный ввод. Пожалуйста, введите 'да' или 'нет'.
Осталось попыток: 1
Записать файл? да
"""

#
# def write_down(question: str,
#                complaint: str = 'Incorrect input. Enter yes or no',
#                retries: int = 4):
#     while retries > 0:
#         answer = input(question).lower()
#         if answer == 'yes':
#             return 1
#         if answer == 'no':
#             return 0
#
#         retries -= 1
#         print(complaint)
#         print(f'Retries left: {retries}')
#
#
# write_down('Do you want exit?')
# print()
# write_down('Dell the file?', 'So exit or not?')
# print()
# write_down('Write down into file?', retries=2)



"""
Задача 2. Накопление значений
При работе со значениями по умолчанию и изменяемыми типами данных нужно знать и
остерегаться ещё одной интересной штуки.
Напишите функцию с двумя аргументами: первый — число num,
позиционный аргумент; второй — список lst, по умолчанию он пустой.
В теле функции в список добавляется число num и сам список выводится на экран.

В основной программе вызовите функции три раза только с одним аргументом (числом), например так:
add_num(5)
add_num(10)
add_num(15)
И посмотрите, что произойдёт.
После этого сделайте значение lst по умолчанию None и поправьте функцию,
чтобы она работала правильно.
"""


#
# def add_num(num, nums=None):
#     nums = nums or []
#     # хитрая конструкция, которая позволит упростить ввод:
#     # if not nums:
#     #    nums = []
#     # Первый вариант будет выбран, если nums не равен None, иначе будет создан и записан пустой список
#     nums.append(num)
#     print(nums)
#
#
# add_num(5)
# add_num(10)
# add_num(15)


"""
Задача 3. Помощь другу
Нашего друга попросили написать функцию, которая на вход принимает список всякого мусора. Ему нужно подготовить из этого списка список словарей, чтобы его коллеги смогли дальше продолжить обработку данных.
Вот список правил, что нужно сделать с изначальным списком:
Если в списке встретился словарь, то оставляем его.
Если в списке встретилась строка, то из неё нужно сделать словарь и положить его в итоговый список,
например  “abc” → {“abc”: “abc”}.
С числами нужно сделать то же самое, что и со строками.
Всё остальное выкидываем из нашего списка.

Друг написал программу, но в ней ошибка, так как она что-то не то выводит :(
Нужна ваша помощь, вот сама программа:

def create_dict(data, template=dict()):
    if isinstance(data, dict):
        return data

    if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        return template[data] = data
 
def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_list.append(create_dict(i_element))
    return new_list
 
data = [“sad”, {“sds”: 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)

 

Исправьте программу и убедитесь, что всё работает верно.
"""

#
# def create_dict(data, template=None):
#     if isinstance(data, dict):
#         return data
#
#     if isinstance(data, (int, float, str)):
#         template = template or dict()
#         template[data] = data
#         return template
#
#
# def data_preparation(old_list):
#     new_list = []
#     for i_element in old_list:
#         new_elem = create_dict(i_element)
#         if new_elem:
#             new_list.append(new_elem)
#     return new_list
#
#
# data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
# data = data_preparation(data)
# print(data)
