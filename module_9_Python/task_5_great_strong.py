print('Задача 5. Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Ему особенно понравилась книга «Преступление и наказание».
# Паоло решил найти самое длинное слово в этой книге, чтобы сравнить его с аналогом на своём языке.

# Что нужно сделать
# Напишите программу, которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.

# Пример:

# Введите текст: Меня зовут Пётр.
# Самое длинное слово, букв: 5.

# Введите текст: Меня зовут Василий
# Самое длинное слово, 7 букв

user_text = input('Ваш текст: ')
max_word = 0
counter = 0

for symbol in user_text:
    if symbol != ' ':
        counter += 1
    else:
        if counter > max_word:
            max_word = counter
        counter = 0

print(f'Самое длинное слово {max_word} букв')



# Поиск минимальной длины слова
# user_text = input('Ваш текст: ')
# min_word = 0
# counter = 0
# is_first_word = True
#
# for symbol in user_text:
#     if symbol != ' ':
#         counter += 1
#         if is_first_word:
#             min_word += 1
#     else:
#         if counter < min_word:
#             min_word = counter
#         if is_first_word:
#             is_first_word = False
#         counter = 0
#
# print(f'Самое короткое слово {min_word} букв')