"""
Задача 2. Поиск элемента — 2
Пользователь вводит искомый ключ.
Если он хочет, то может ввести максимальную глубину — уровень,
до которого будет просматриваться структура.

Напишите функцию, которая находит заданный пользователем ключ в словаре и
выдаёт значение этого ключа на экран.
По умолчанию уровень не задан. В качестве примера можно использовать такой словарь:

site = {
'html': {
'head': {
'title': 'Мой сайт'
},
'body': {
'h2': 'Здесь будет мой заголовок',
'div': 'Тут, наверное, какой-то блок',
'p': 'А вот здесь новый абзац'
}
}
}

Пример 1
> Введите искомый ключ: head
> Хотите ввести максимальную глубину? Y/N: n
> Значение ключа: {'title': 'Мой сайт'}

Пример 2
> Введите искомый ключ: head
> Хотите ввести максимальную глубину? Y/N: y
> Введите максимальную глубину: 1
> Значение ключа: None
"""


def search_element(struct: dict, key: str, deep=None) -> str:
    result = None
    if deep == 0:
        return result

    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if not isinstance(sub_struct, dict):
            continue
        result = search_element(sub_struct, key, deep - 1 if deep else None)
        if result:
            break

    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


user_key = input('Enter a key for search: ')
user_deep = None
flag_deep = input('Do you want to enter max deep? Y/N ').lower()
if flag_deep == 'y':
    user_deep = int(input('Enter max deep: '))

value = search_element(site, user_key, deep=user_deep)

if value:
    print(f'Result: {value}')
else:
    print('There is no such key')
