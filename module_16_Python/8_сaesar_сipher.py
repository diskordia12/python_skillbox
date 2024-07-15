"""
Задание 8. Шифр Цезаря
Юлий Цезарь использовал свой способ шифрования текста.
Каждая буква заменялась на следующую по алфавиту через K позиций по кругу.
Если взять русский алфавит и K, равное 3,
то в слове, которое мы хотим зашифровать, буква А станет буквой Г, Б станет Д и так далее.
Пользователь вводит сообщение и значение сдвига.
Напишите программу, которая изменит фразу при помощи шифра Цезаря.

Пример:
> Введите сообщение: это питон.
> Введите сдвиг: 3
> Зашифрованное сообщение: ахс тлхср.
"""

capital_alphabet = [chr(ord('A') + alphabetIndex) for alphabetIndex in range(0, 26)]
print(capital_alphabet)
lower_alphabet = [chr(ord('a') + alphabetIndex) for alphabetIndex in range(0, 26)]
print(lower_alphabet)

merge_alphabet = [letter1 + letter2 for letter1, letter2 in zip(capital_alphabet, lower_alphabet)]
merge_alphabet = ''.join(merge_alphabet)
print(merge_alphabet)

user_message = input('Say something: ')
shift = int(input('Shift: '))

cipher_message = [(merge_alphabet[(merge_alphabet.index(letter) + shift * 2) % 52] if letter in merge_alphabet
                  else letter)
                  for letter in user_message]

print(f'Cipher message: {"".join(cipher_message)}')


#
# Solution without merged alphabet by Aleksei
# def get_shifted(letter, shift):
#     if ord('a') <= ord(letter) <= ord('z'):
#         return lower_alphabet[lower_alphabet.index(letter) + shift % 26]
#     elif ord('A') <= ord(letter) <= ord('Z'):
#         return capital_alphabet[capital_alphabet.index(letter) + shift % 26]
#     else:
#         return letter
#
#
# cipher = [get_shifted(letter, shift) for letter in user_message]


# Solution with casting all letters to a upper case
# cipher_message = [(whole_alphabet[(whole_alphabet.index(letter) + shift) % 26] if letter in whole_alphabet
#                   else letter)
#                   for letter in user_message]

# user_message = user_message.split(' ')
# cipher_message = [[alphabet[(alphabet.index(letter) + shift) % 26] for letter in word]
#                    for word in user_message]


# # Print put for my method wit list of words
# print('Cipher message: ', end='')
# for word in cipher_message:
#     for letter in word:
#         print(letter, end='')
#     print(end=' ')



