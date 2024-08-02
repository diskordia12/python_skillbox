"""
Задание 4. Гистограмма частоты — 2
Вы уже писали программу для лингвистов, которая получала на вход текст и считала,
сколько раз каждый символ встречается в строке.
Теперь задание изменилось: максимальную частоту выводить не нужно, но необходимо написать функцию,
которая будет инвертировать полученный словарь.
То есть в качестве ключа будет частота, а в качестве значения — список символов с этой частотой.

По итогу нужно реализовать следующие подзадачи:
- получить текст и создать из него оригинальный словарь частот;
- создать новый словарь и заполнить его данными из оригинального словаря частот,
используя количество повторов в качестве ключей,
а буквы — в качестве значений, добавляя их в список для хранения.

Пример
> Введите текст: здесь что-то написано
> Оригинальный словарь частот:
> : 2
> - : 1
> З : 1
> а : 2
> д : 1
> е : 1
> и : 1
> н : 2
> о : 3
> п : 1
> с : 2
> т : 2
> ч : 1
> ь : 1
> Инвертированный словарь частот:
> 1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
> 2 : ['с', ' ', 'т', 'н', 'а']
> 3 : ['о']
"""


def get_frequencies(text: str) -> dict:
    frequency = dict()
    for sym in text:
        if sym in frequency:
            frequency[sym] += 1
        else:
            frequency[sym] = 1
    return frequency


user_text = input('Your text: ')
sym_frequency = get_frequencies(user_text)
print(f'Frequency: ')
for sym, freq in sorted(sym_frequency.items()):
    print(f'{sym}: {freq}')
print()

reverse_frequency = dict()

for symbol, frequency in sym_frequency.items():
    if frequency not in reverse_frequency:
        reverse_frequency[frequency] = list()

    reverse_frequency[frequency] += symbol


print('Inverted dictionary of frequencies:')
for freq, sym in reverse_frequency.items():
    print(f'{freq}: {sym}')
    