"""
Задание 7. Анализ слова — 2
Что нужно сделать
Продолжите писать анализаторы для текста.
Теперь необходимо реализовать код, с помощью которого можно определять палиндромы,
то есть слова, которые читаются одинаково слева направо и справа налево.

Пример 1:
> Введите слово: мадам
> Слово является палиндромом

Пример 2:
> Введите слово: abccba
> Слово является палиндромом
Пример 3:
> Введите слово: abbd
> Слово не является палиндромом
"""


word = input("Enter a word: ")
word = list(word)
if word == word[::-1]:
    print('This is a palindrome')
else:
    print('This is not a palindrome')


"""
Way only with cycle, without slicing
"""
print('\nWay only with cycle, without slicing')

for i in range(len(word)):
    if word[i] != word[-i-1]:
        print('This is not a palindrome')
        break
else:
    print('This is a palindrome')
