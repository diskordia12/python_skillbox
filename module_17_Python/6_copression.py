"""
Задание 6. Сжатие
Из-за того, что объём данных увеличился, понадобилось сжать эти данные,
но так, чтобы не потерять важную информацию.
Для этого было придумано специальное кодирование: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'.
То есть группы одинаковых символов исходной строки заменяются
на эти символы и количество их повторений в строке.
Напишите программу, которая считывает строку, кодирует её,
используя предложенный алгоритм, и выводит закодированную последовательность на экран.
Код должен учитывать регистр символов.

Пример
Введите строку: aaAAbbсaaaA.
Закодированная строка: a2A2b2с1a3A1.
"""


def compression(text: str) -> list:
    coded_message = ''
    counter = 1
    previous = text[0]
    for sym in text[1:]:
        if sym == previous:
            counter += 1
        else:
            coded_message += previous + str(counter)
            counter = 1
        previous = sym

    coded_message += previous + str(counter)

    return coded_message


message = input('Your message: ')

print(f'Coded message: {compression(message)}')


# My old solution with slicing
# def compression(text: str) -> list:
#     coded_message = list()
#     counter = 1
#     for i_sym in range(len(text)):
#         if text[i_sym] == text[i_sym + 1: i_sym + 2]:
#         # if text[i_sym] == text[(i_sym + 1) % len(text)]:
#             counter += 1
#             continue
#         coded_message.extend(''.join([text[i_sym], str(counter)]))
#         counter = 1
#
#     return coded_message

#
# message = input('Your message: ')
#
# print(f'Coded message: {"".join(compression(message))}')







