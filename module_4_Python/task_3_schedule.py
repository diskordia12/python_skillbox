print('Task 3. schedule')

# После выполненной задачи Вася устал и понял, что весь следующий день ему придётся восстанавливать силы. Вася решил, что работать он будет только в чётные дни и написал небольшую программу, которая поможет ему не пропустить рабочий день.

# Напишите программу, которая проверяет, чётное ли число ввёл пользователь, и выводит соответствующее сообщение.

# Подсказка: для проверки чётности используйте оператор %.

date = int(input('Enter the number od day: '))
if date%2 == 0:
    print('Today is an even day. Work!')
else:
    print('Today is an odd day. Rest!')
