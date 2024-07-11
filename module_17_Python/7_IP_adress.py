"""
Задание 7. IP-адрес 2
При написании клиент-серверного приложения часто приходится работать с IP-адресами.
Как вы уже знаете, IP-адрес состоит из четырёх целых чисел в диапазоне от 0 до 255,
разделённых точками.
Пользователь вводит строку. Напишите программу, которая определяет, действительно ли заданная строка
— правильный IP-адрес. Обеспечьте контроль ввода, где предусматривается
добавление целых чисел от 0 до 255 и точек между ними.

Пример 1
> Введите IP: 128.16.35.a4
> a4 — это не целое число.

Пример 2
> Введите IP: 240.127.56.340
> 340 превышает 255.

Пример 3
> Введите IP: 34.56.42,5
> Адрес — это четыре числа, разделённые точками.

Пример 4
> Введите IP: 128.0.0.255
> IP-адрес корректен.
"""


def check_numbers(text: str) -> None:
    for num in text.split('.'):
        if not num.isdigit():
            raise ValueError(f'{num} is not integer number')


def check_interval(text: str) -> None:
    for num in text.split('.'):
        if int(num) < 0 or int(num) > 255:
            raise ValueError(f'Wrong {num}. Only from 0 to 255')


while True:
    ip_address = input('Enter IP: ')
    if ip_address.count('.') != 3:
        print('IPv4 address is four numbers separated by dot')
        continue

    try:
        check_interval(ip_address)
        check_numbers(ip_address)
    except ValueError as e:
        print(f'Error: {e}')

    print('IPv4 address is correct')


# # My old solution
# def is_numbers(text: str) -> bool:
#     text = text.split('.')
#     for num in text:
#         if not num.isdigit():
#             print(f'{num} is not integer number')
#             return False
#     return True
#
#
# def is_interval(text: str) -> bool:
#     text = text.split('.')
#     for num in text:
#         if int(num) < 0 or int(num) > 255:
#             print(f'Wrong {num}. Only from 0 to 255')
#             return False
#     return True
#
#
# while True:
#     ip_address = input('Enter IP: ')
#     if ip_address.count('.') != 3:
#         print('IP address is four numbers separated by dot')
#         continue
    #
    # if not is_numbers(ip_address):
    #     continue
    #
    # if not is_interval(ip_address):
    #     continue
    #
    # print('IP-address is correct')
