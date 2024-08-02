"""
Задание 5. Словарь синонимов
Одна библиотека поручила вам написать программу для оцифровки словарей синонимов.
На вход в программу подаётся N пар слов. Каждое слово является синонимом для своего парного слова.
Реализуйте код, который составляет словарь синонимов (все слова в словаре различны),
затем запрашивает у пользователя слово и выводит на экран его синоним.
Обеспечьте контроль ввода: если такого слова нет, выведите ошибку и запросите слово ещё раз.
При этом проверка не должна зависеть от регистра символов.

Пример
> Введите количество пар слов: 3
> Первая пара: Привет — Здравствуйте
> Вторая пара: Печально — Грустно
> Третья пара: Весело — Радостно
> Введите слово: интересно
> Такого слова в словаре нет.
>
> Введите слово: здравствуйте
> Синоним: Привет
"""

amount = int(input('Enter amount pair of words: '))
synonyms = dict()

for i in range(amount):
    word_pair = input(f'{i + 1} - pair: ').split(' - ')
    synonyms[word_pair[0].upper()] = word_pair[1].upper()
    synonyms[word_pair[1].upper()] = word_pair[0].upper()

print(synonyms)

user_word = input('Enter your word: ').upper()

if user_word in synonyms:
    print(f'Synonym: {synonyms[user_word]}')
    # for first_word, second_word in synonyms.items():
    #     if second_word == user_word:
    #         print(f'Synonym: {first_word}')
    #         break
else:
    # print(f'{synonyms.get(user_word, "There is no such wor in dict")}')
    print('There is no such wor in dict')

