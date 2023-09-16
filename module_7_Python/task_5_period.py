print('Task 5. Period')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

# (среднее арифметическое можно посчитать поделив сумму подходящих чисел на их количество)

a = int(input(f'Enter the beginning of the segment а = '))
b = int(input(f'Enter the end of the segment b = '))
sum_numbers = 0
amount_numbers = 0


# counter = 0
for number in range(a, b + 1):
    # counter += 1
    if number % 3 == 0:
        sum_numbers += number
        amount_numbers += 1

print(f'Среднее арифметическое всех чисел из отрезка [{a}; {b}],'
      f' которые кратны числу 3 равно {sum_numbers/amount_numbers}')


# Более эффективное решение
# Найти ближайшее к а сверху число, делящееся на 3
# Найти ближайшее к b снизу число, делящееся на 3
# Идти в цикле от start к end с шагом три
# Эффективность -в три раза меньше итераций цикла

sum_numbers = 0
amount_numbers = 0

remainder_a = a % 3
start = a + (0 if remainder_a == 0 else 3 - remainder_a)

remainder_b = b % 3
end = b
if remainder_b != 0:
    end -= b % 3

print(f'start = {start}')
print(f'end = {end}')

counter = 0

for number in range(start, end + 1, 3):
    counter += 1
    sum_numbers += number
    amount_numbers += 1

print(f'Количество итераций: {counter}')

print(f'Среднее арифметическое всех чисел из отрезка [{a}; {b}],'
      f' которые кратны числу 3 равно {sum_numbers/amount_numbers}')

