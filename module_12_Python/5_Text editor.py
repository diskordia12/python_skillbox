"""
Мы продолжаем разрабатывать новый текстовый редактор,
и в этот раз нам поручили написать для него код,
который считает количество любой буквы
и любой цифры в тексте (а не только буквы Ы как раньше).

Напишите функцию count_letters,
которая принимает на вход текст и подсчитывает,
какое в нём количество цифр K и букв N.

Функция должна вывести на экран информацию
о найденных буквах и цифрах в определенном формате.

Пример:
> Введите текст: 100 лет в обед
> Какую цифру ищем? 0
> Какую букву ищём? л

> Количество цифр 0: 2
> Количество букв л: 1
"""


def count_symbols(text: str, desire_symbol: str) -> int:
    return text.count(desire_symbol)
    # counter = 0
    # for symbol in text:
    #     if symbol == desire_symbol:
    #         counter += 1
    # return counter


user_text = input('Enter your text: ')
desired_digit = input('What digit to search: ')
desired_letter = input('What letter to search: ')

print(f'Amount of digits {desired_digit}: {count_symbols(user_text, desired_digit)}')
print(f'Amount of letters {desired_letter}: {count_symbols(user_text, desired_letter)}')
