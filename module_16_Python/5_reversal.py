"""
Задание 5. Разворот
На вход в программу подаётся строка, в которой буква h встречается как минимум два раза.
Реализуйте код, который разворачивает последовательность символов,
заключённую между первым и последним появлением буквы h, в противоположном порядке.
Пример 1:
Введите строку: hqwehrty
Развёрнутая последовательность между первым и последним h: ewq.

Пример 2:
Введите строку: hh
Развёрнутая последовательность между первым и последним h:

Пример 3:
Введите строку: hhqwerh
Развёрнутая последовательность между первым и последним h: rewqh.

Советы и рекомендации
Индекс нужного элемента можно искать как вручную, так и при помощи готовых методов списка.
У метода index есть «брат» — метод rindex.
В отличие от первого второй метод начинает поиск с правой стороны (с конца).
"""

user_message = input('Your message: ')
index_first_h = user_message.index('h')
# # using .rindex
index_last_h = user_message.rindex('h')
# reverse message and use just .index
# index_last_h = len(user_message) - 1 - user_message[::-1].index('h')


reverse_message = user_message[index_last_h - 1: index_first_h: -1]
print(f'Reversed message between first h and last one: {reverse_message}')
