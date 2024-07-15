"""
Задание 2. Турнир
Для двух дней соревнований по волейболу необходимо сформировать турнирную сетку
из восьми человек. На первый день из списка участников решили выбрать каждого второго.
Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар.
Напишите программу, которая выводит элементы списка только с чётными индексами.

Пример:
> Первый день: ['Артемий', 'Влад', 'Дима', 'Женя']
"""

names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

first_day = [names[i_name] for i_name in range(0, len(names), 2)]
print(f'The first day: {first_day}')
