"""
Задание 1. Меню ресторана
Ресторан заказал вам приложение, которое в один клик отображает пользователю меню.
Для работы ресторан предоставил вам свой сайт, где можно найти меню в виде идущих подряд
названий блюд.
Напишите программу, которая выводит меню на экран.
На вход подаётся строка из названий блюд, разделённых символом «;»,
а на выходе названия перечисляются через запятую и пробел.

Пример:
> Доступное меню: утиное филе;фланк-стейк;банановый пирог;плов.
> Сейчас в меню есть: утиное филе, фланк-стейк, банановый пирог, плов.
"""

current_menu = 'утиное филе;фланк-стейк;банановый пирог;плов'
current_menu = current_menu.split(';')
current_menu = ', '.join(current_menu)

# Solution with replace method
# current_menu = current_menu.replace(';', ', ')

print(f'Menu available now: {current_menu}')
