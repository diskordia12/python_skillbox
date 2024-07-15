"""
Задание 6. Бегущие цифры
Что нужно сделать
Вы пишете программу для маленького табло, в котором циклически повторяется один и тот же текст
или числа, например как в метро, автобусах или трамваях.
Дан список из N элементов и целое число K.
Напишите программу, которая циклически сдвигает элементы списка вправо на K позиций.
Используйте минимально возможное количество операций присваивания.

Пример 1:
> Сдвиг: 1
> Изначальный список: [1, 2, 3, 4, 5]
> Сдвинутый список: [5, 1, 2, 3, 4]
Пример 2:
> Сдвиг: 3
> Изначальный список: [1, 4, –3, 0, 10]
> Сдвинутый список: [–3, 0, 10, 1, 4]
"""
size = int(input('Enter size of your string: '))
user_list = list()

for i in range(size):
    sym = input('Enter a symbol: ')
    user_list.append(sym)

shift = int(input('Enter a shift: '))
shift %= len(user_list)

shifted_list = list()
shifted_list = user_list[-shift:] + user_list[:-shift]
print(f'Original list: {user_list}')
print(f'Shifted list: {shifted_list}')

"""
Way only with cycle, without slicing
"""
# shift = int(input('Enter a shift: '))
# shift = shift % len(user_list)
#
# shifted_list = list()
#
# for i in range(-shift, len(user_list) - shift):
#     shifted_list.append(user_list[i])
#
# print(f'Original list: {user_list}')
# print(f'Shifted list: {shifted_list}')

"""
list comprehensions
"""
# shifted_list = [user_list[i] for i in range(-shift, len(user_list) - shift)]



