print('Task 3. big_numbers')

# У неудачливого бухгалтера всё опять идёт наперекосяк:
# ему приносят такие большие счета, что числа не помещаются на бумаге.

# Напишите программу, которая считала бы для него, сколько цифр во вводимом числе.
# Обратите внимание, что число 0 имеет одну цифру.

# Пример:
# Введите число: 567
# Ответ: 3

# Введите число: 1203
# Ответ: 4

number = int(input('Enter number: '))
# numbers_count= 0
# while number > 10:
#     number //= 10
#     numbers_count +=1
# print(f'Количество цифр: {numbers_count+1}')


numbers_count= 0
while number > 0:
    numbers_count += 1
    number = number // 10
print(f'Number of digits: {numbers_count}')

