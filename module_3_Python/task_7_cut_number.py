print('Task 7. Cut number')

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

number = int(input('Enter the 4-digit number:'))
first_digit = number // 1000
second_digit = (number % 1000) // 100
third_digit = (number % 100) // 10
fourth_digit = number % 10
print(first_digit, second_digit, third_digit, fourth_digit)
reverse_number = fourth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit
print(f'Reverse number: {reverse_number}')

