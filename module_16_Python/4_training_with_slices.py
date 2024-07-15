"""
Задание 4. Тренировка со срезами
Дана строка, в которой хранятся первые семь букв английского алфавита.
alphabet = 'abcdefg'
Напишите программу, которая выводит на экран десять таких результатов:
- копию строки;
- элементы строки в обратном порядке;
- каждый второй элемент строки (включая самый первый);
- каждый второй элемент строки после первого;
- все элементы до второго;
- все элементы, начиная с конца до предпоследнего;
- все элементы в диапазоне индексов от 3 до 4 (не включая 4);
- последние три элемента строки;
- все элементы в диапазоне индексов от 3 до 4;
- то же, что и в предыдущем пункте, но в обратном порядке.
Для получения и вывода результатов используйте только команду print и срезы.
Результаты работы программы:
> 1: abcdefg
> 2: gfedcba
> 3: aceg
> 4: bdf
> 5: a
> 6: g
> 7: d
> 8: efg
> 9: de
> 10: ed
"""

alphabet = 'abcdefg'

print(f'1 - копия строки: {alphabet[:]}')
print(f'2 - элементы строки в обратном порядке: {alphabet[::-1]}')
print(f'3 - каждый второй элемент строки (включая самый первый): {alphabet[::2]}')
print(f'4 - каждый второй элемент строки после первого: {alphabet[1::2]}')
print(f'5 - все элементы до второго: {alphabet[:1]}')
print(f'6 - все элементы, начиная с конца до предпоследнего: {alphabet[:-2:-1]}')
print(f'7 - все элементы в диапазоне индексов от 3 до 4 (не включая 4): {alphabet[3:4]}')
print(f'8 - последние три элемента строки: {alphabet[-3:]}')
print(f'9 - все элементы в диапазоне индексов от 3 до 4: {alphabet[3:4 + 1]}')
print(f'10 - то же, что и в предыдущем пункте, но в обратном порядке: {alphabet[4:3 - 1:-1]}')
