# Задача 1. Таблица кубов
# Паше для проекта по математике нужна таблица кубов (третья степень числа) только чётных чисел от 1 до N.
# Напишите программу, которая выведет ему эту таблицу на экран.
# Не используйте условные операторы.

# n = int(input('Введите число:'))
#
# for number in range(1,n//2 + 1):
#     number *= 2
#     print(f'{number} ** 3 = {number**3}')



# Задача 2. Деление клетки
# В одной лаборатории наблюдают за одноклеточной амёбой.
# Мы знаем, что каждые три часа она делится на 2 клетки.
# Нам нужно для этой лаборатории написать программу, которая будет выводить сколько прошло часов
# и сколько получилось клеток.
# Также нас попросили писать на каждом этапе деления сколько осталось часов до завершения наблюдения,
# чтобы ученым было проще формулировать выводы на определённом этапе наблюдения.

# total_hour = int(input('Введите сколько часов будет длиться наблюдение: '))
# cells = 1

# for hour in range(1, total_hour // 3 + 1):
#     cells *= 2
#     print(f'Прошло часов {hour*3}')
#     print(f'Количество клеток сейчас: {cells}')
#     print(f'Осталось {total_hour-hour*3} часов \n')
#
# print('Наблюдение завершено!')



# Задача 3. Квадраты нечётных чисел
# Вводится число N. Напишите программу, которая выводит квадраты нечетных чисел от 1 до N.
# Нельзя использовать условные операторы. Можно использовать цикл while,
# но постарайтесь всё-таки решить с помощью конструкции for in range.

# n = int(input('Введите число:'))
#
# for number in range(1, n // 2 + n % 2 + 1):
#     print(number)
#     number = number * 2 - 1
#     print(f'{number} ** 2 = {number**2}')


# Задача 1. Степень нечётного числа
# Выведите третью степень каждого нечётного числа в диапазоне от
# единицы до указанного пользователем числа включительно.
# Для этого используйте шаг внутри функции range.

# n = int(input('Введите число:'))
#
# for number in range(1, n + 1, 2):
#     print(f'{number} **3 = {number ** 3}')



# Задача 2. Театр
# Ваню заставили пойти в театр на балет.
# Ему стало там настолько скучно, что он придумал себе очень странное развлечение:
# считать сумму номеров каждого пятого стула в рядах.
#
# Напишите программу для вычисления суммы каждого пятого числа,
# лежащего в диапазоне от единицы до N. Использовать условный оператор нельзя.
#
# Пример:
#
# Введите число: 21
# Номер стула: 1
# Номер стула: 6
# Номер стула: 11
# Номер стула: 16
# Номер стула: 21
# Сумма: 55

# n = int(input('Введите число: '))
# chair_sum = 0
# for chair in range(1, n + 1, 5):
#     print(f'Номер стула: {chair}')
#     chair_sum += chair
#
# print(f'Сумма: {chair_sum}')

# Задача 3. Диета
# Саша просыпается когда угодно, но в 23 часа уже точно идёт спать.
# Питается Саша следующим образом: каждые 3 часа он выпивает литр воды и съедает N калорий.
# Пить и есть он, кстати, начинает сразу как только проснётся. Напишите программу,
# которая считает сколько он выпьет литров воды и сколько калорий он съест перед тем как пойдёт спать.

# wake_up = int(input('Время пробуждения: '))
# water = 0
# calories_sum = 0
#
# for hour in range(wake_up, 23, 3):
#     water += 1
#     calories = int(input('Сколько калорий съел: '))
#     calories_sum += calories
#
# print(f'Выпито {water} литров воды и'
#       f'съедено {calories_sum} калорий')


# Задача 1. Прятки
# Наверное, все мы в детстве играли в прятки. И конечно же всегда был “голя” - тот, кто всех ищет.
# И пока все прячутся, он с закрытыми глазами ведёт обратный отсчёт секунд.
#
# Напишите программу, которая получает на вход количество секунд N и выводит все числа от N до 1
# в порядке убывания. В конце выведите сообщение “Я иду искать!”
#
# Пример:
# Введите кол-во секунд: 5
# 5
# 4
# 3
# 2
# 1
# Я иду искать!

# n = int(input('Введите число: '))
# # for number in range(n, 0, -1):
#     print(number)
# # print('Я иду искать!')



# Задача 2. Армия
# У офицера сегодня очень плохое настроение: он выстроил всех солдат в шеренгу и, начиная с конца,
# начал спрашивать у каждого четвёртого солдата сколько правил прописано в воинском уставе.
# Количество правил с каждым разом меняется. Если солдат ответил неверно, то применяется закон под названием
# “упал-отжался”. Количество отжиманий считается как 10 умножить на порядковый номер солдата в шеренге.
# Напишите программу, которая посчитает сколько в сумме получится таких отжиманий.
#
# Усложнение: напишите программу так, чтобы офицер начинал спрашивать не с последнего солдата в шеренге,
# а с четвертого с конца. Если солдат в шеренге слишком мало, офицер не спрашивает никого

# total_soldiers = int(input('Кол-во солдат: '))
# total_rules = 1
# push_ups_sum = 0
#
# for soldier in range (total_soldiers-3, 0, -4):
#     total_rules = (total_rules + soldier * 3) % total_soldiers
#     soldier_rules = int(input('Солдат, назови кол-во правил: '))
#     if soldier_rules != total_rules:
#         print(f'Неверно! {soldier * 10} отжиманий!')
#         push_ups_sum += soldier * 10
#
# print(f'Всего отжиманий: {push_ups_sum}')


# Задача 3. Прятки 2
# Пока все прятались, “голя” решил схитрить и считать секунды быстрее, чем нужно.
#
# Напишите программу, которая выводит только чётные числа в порядке убывания от N до 1 включительно,
# используя цикл for. Нельзя использовать условный оператор.

n = int(input('Введите число: '))
    # even_n = n - n % 2  # n%2 для чётных чисел будет равно 0, для нечетных будет равно 1, таким образом мы из числа n всегда будем получать
#    # чётное число
#       for i in range(even_n, 0, -2):
for number in range(n - n%2, 0-1, -2):
    print(number)
print('Я иду искать!')

