print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

a = int(input('Начало отрезка a = '))
b = int(input('Конец отрезка b = '))
c = int(input('Введите любое число внутри отрезка с = '))
sum_numbers = 0
amount_numbers = 0

remainder_a = a % c
start = a + (0 if remainder_a == 0 else c - remainder_a)

remainder_b = b % c
end = b
if remainder_b != 0:
    end -= b % c

print(f'start = {start}')
print(f'end = {end}')

for number in range(start, end + 1, c):
    sum_numbers += number
    amount_numbers += 1

print(f'Среднее арифметическое всех чисел из отрезка [{a}; {b}],'
      f' которые кратны числу {c} равно {sum_numbers/amount_numbers}')
