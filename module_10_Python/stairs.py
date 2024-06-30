
# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

size = int(input('Enter a number: '))

for row in range(1, size + 1):
    for col in range(row):
        print(row, end='\t')
    print()
