"""
Задача 1. Свой for (ну почти)
Дан любой итерируемый объект, например список из N чисел.
Реализуйте функцию, которая эмулирует работу цикла for с помощью цикла while и
проходит во всем элементам итерируемого объекта. Не забудьте про исключение «конца итерации».
"""
import random

# numbers = [1, 55, 2, 33, 3, 44]
#
# iterator = numbers.__iter__()
#
# while True:
#     try:
#         print(iterator.__next__())
#     except StopIteration:
#         break
#


"""
Задача 1. Бесконечный итератор
Реализуйте итератор-счётчик, который не принимает никаких атрибутов
и имеет только один статический атрибут — счётчик.
Итератор увеличивает счётчик и возвращает предыдущее значение.
У вас должен получиться бесконечный итератор.

То есть при вызове такого кода в основной программе
my_iter = СountIterator()
for i_elem in my_iter:
    print(i_elem)
значения будут выдаваться бесконечно.
"""

#
# class CountIterator:
#
#     def __init__(self):
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         return self.counter - 1
#
#
# my_iter = CountIterator()
# for elem in my_iter:
#     print(elem)



"""
Задача 2. Случайная сумма
Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и
предыдущего элемента (первый элемент — просто случайное вещественное число от 0 до 1).
Алексею нельзя хранить в памяти весь этот список, а со значениями работать как-то надо.
Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу.
Также сделайте, чтобы при каждом новом вызове итератора в цикле значения считались заново.

Пример работы программы:
Кол-во элементов: 5
Элементы итератора:
0.74
1.13
1.95
2.2
2.55
Новое кол-во элементов: 6
Элементы итератора:
0.79
1.58
2.55
2.81
3.06
3.34
"""

#
# class SumOfLastTwo:
#
#     def __init__(self, count):
#         self.first_number = round(random.uniform(0, 1), 2)
#         self.last = 0
#         self.end = count
#         self.start = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start > self.end:
#             raise StopIteration
#         self.last += round(random.uniform(0, 1), 2)
#         return self.last
#
#
# counter = SumOfLastTwo(5)
# for i in counter:
#     print(i)
#
# print()
# counter = SumOfLastTwo(6)
# for i in counter:
#     print(i)


"""
Задача 3. Простые числа
Реализуйте класс-итератор Primes, который принимает максимальное число N
и выдаёт все простые числа от 1 до N. 

Основной код:
prime_nums = Primes(50)
for i_elem in prime_nums:
    print(i_elem, end=' ')
Ожидаемый результат кода:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
"""

#
# class Primes:
#
#     def __init__(self, n: int):
#         self.end = n
#         self.start = 1
#         self.prime_numbers = list()
#
#     def __iter__(self):
#         # self.start = 1
#         return self
#
#     def __next__(self):
#         self.start += 1
#         for digit in range(self.start, self.end + 1):
#             for prime in self.prime_numbers:
#                 if digit % prime == 0:
#                     break
#             else:
#                 self.start = digit
#                 self.prime_numbers.append(digit)
#                 return self.start
#         raise StopIteration
#
#
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
#
# print()
# prime_nums = Primes(10)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')


"""
Задача 1. Бесконечный генератор
По аналогии с бесконечным итератором из практики предыдущего урока,
реализуйте свой счётчик-генератор, который также в цикле будет бесконечно выдавать значения.

Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.
"""

#
# def my_generator():
#     start = 0
#     while True:
#         yield start
#         start += 1
#
#
# def get_prime_numbers(n: int):
#     prime_numbers = list()
#     for digit in range(2, n + 1):
#         for prime in prime_numbers:
#             if digit % prime == 0:
#                 break
#         else:
#             prime_numbers.append(digit)
#             yield digit
#
#
# # my_gen = my_generator()
# # for elem in my_gen:
# #     print(elem)
#
# primes = get_prime_numbers(50)
# for number in primes:
#     print(number, end='\t')



"""
Задача 2. Очень большой файл
Вам на обработку пришёл огромнейший файл с данными.
Настолько огромный, что при его открытии компьютер просто зависает,
так как данные не помещаются в оперативной памяти вашего суперкомпьютера (не очень-то и «супер»).

В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки.
Напишите программу, которая подсчитает общую сумму чисел в файле.
Для считывания файла реализуйте специальный генератор.
"""


def numbers_from_text(text):
    return [int(number) for number in text.rstrip().split()]


def file_parser(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            clear_line_sum = sum(numbers_from_text(line))
            yield clear_line_sum


all_sum = 0
for number in file_parser("numbers.txt"):
    all_sum += number

print("Вариант №1", all_sum)


# Ещё один вариант решения с функцией map()
def file_parser(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            clear_line_sum = sum(map(int, line.rstrip().split()))
            yield clear_line_sum


all_sum = 0
for number in file_parser("numbers.txt"):
    all_sum += number

print("Вариант №2", all_sum)


