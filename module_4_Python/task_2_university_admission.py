print('Task 2. Admission')

# Вася работает разработчиком, и его компания создаёт сайт для образовательной компании. Заказчики попросили реализовать калькулятор баллов ЕГЭ в помощь поступающим. Эту задачу отдали Васе.

# Напишите программу, которая запрашивает у пользователя результаты ЕГЭ по трём экзаменам, и проверяет, поступил ли он на бюджет. Проходной балл равняется 270. Выведите соответствующее сообщение.

# Пример 1:
# Введите количество баллов по русскому языку: 90
# Введите количество баллов по математике: 90
# Введите количество баллов по информатике: 90

# Поздравляю, ты поступил на бюджет!

# Пример 2:
# Введите количество баллов по русскому языку: 100
# Введите количество баллов по математике: 50
# Введите количество баллов по информатике: 70

# К сожалению, ты не прошёл на бюджет.
rus_language = int(input('Enter of points in Russian language: '))
math = int(input('Enter of points in mathematics: '))
computer_science = int(input('Enter of points in computer science: '))
if rus_language + math + computer_science >= 270:
    print('Congratulations, you have entered the budget!')
else:
    print('Unfortunately, you didn\'t pass the budget.')
