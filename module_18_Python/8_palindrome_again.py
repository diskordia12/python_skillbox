"""
Задание 8. Снова палиндром
Пользователь вводит строку.
Необходимо написать программу, которая определяет, существует ли у этой строки перестановка,
при которой она станет палиндромом. Затем она должна выводить соответствующее сообщение.

Пример 1
Введите строку: aab
Можно сделать палиндромом

Пример 2
Введите строку: aabc
Нельзя сделать палиндромом
"""
# mama
# mabam - 5

#
# aaabc - 5
# abc - 3

def get_frequencies(text: str) -> dict:
    frequency = dict()
    for sym in text:
        if sym in frequency:
            frequency[sym] += 1
        else:
            frequency[sym] = 1
    return frequency


user_text = input('Enter your text: ')

sym_frequencies = get_frequencies(user_text)
odd_count = 0
print(sym_frequencies)

for freq in sym_frequencies.values():
    if freq % 2 != 0:
        odd_count += 1
print(odd_count)

if odd_count <= 1:
    print('Can be converted to a palindrome')
else:
    print('Can\'t be converted to a palindrome')

# Second way with set
print('\nSecond way')

control_set = set()
for symbol in user_text:
    if symbol in control_set:
        control_set.remove(symbol)
    else:
        control_set.add(symbol)

if len(control_set) <= 1:
    print('Can be converted to a palindrome')
else:
    print('Can\'t be converted to a palindrome')








