print('Task 6. Finance audit')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79

first_number = int(input('Enter the first number:'))
second_number = int(input('Enter the second number:'))
first_remainder = first_number % 10**2
second_remainder = second_number % 10**2
print(first_remainder + second_remainder)
