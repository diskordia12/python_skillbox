"""
Задание 8. Симметричная последовательность
Последовательность чисел называется симметричной, если она одинаково читается как слева направо,
так и справа налево. Например, следующие последовательности являются симметричными:
1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1
Пользователь вводит последовательность из N чисел.
Напишите программу, которая определяет, какое минимальное количество и каких чисел нужно добавить
в конец этой последовательности, чтобы она стала симметричной.

Пример 1:
> Количество чисел: 5
> Число: 1
> Число: 2
> Число: 1
> Число: 2
> Число: 2
> Последовательность: [1, 2, 1, 2, 2]
> Нужно приписать чисел: 3
> Сами числа: [1, 2, 1]

Пример 2:
> Количество чисел: 5
> Число: 1
> Число: 2
> Число: 3
> Число: 4
> Число: 5
> Последовательность: [1, 2, 3, 4, 5]
> Нужно приписать чисел: 4
> Сами числа: [4, 3, 2, 1]

Советы и рекомендации
Убедитесь, что ваш алгоритм работает с разными последовательностями, например с такими:
[1, 2, 1] — в этом случае ничего добавлять не нужно.
[1, 2, 3, 4, 3] — в этом случае надо добавить минимум, то есть числа 2 и 1.
"""
# 1 2 3 4 3 3 4 3 2 1
#
# 3 4 3 2 1


def is_symmetric(numbers: list) -> bool:
    return numbers == numbers[::-1]


numbers_amount = int(input('Amount of numbers: '))
sequence = [int(input('Number: ')) for num in range(numbers_amount)]
print(f'\nInitial sequence: {sequence}')

additional_numbers = list()

if is_symmetric(sequence):
    print(f'Sequence is already symmetric: {sequence}')
    exit(0)

# If you think why len(sequence) - 1:
# len(sequence) would make no sense
# For example
# Assume we have an array [1, 2, 3, 4]
# Then [1, 2, 3, 4, 3, 2, 1] and [1, 2, 3, 4, 4, 3, 2, 1] are both symmetric,
# and we are looking for the least amount of numbers
# That will work for any array
for i in range(len(sequence) - 1):
    additional_numbers = sequence[i::-1]
    if is_symmetric(sequence + additional_numbers):
        break

print(f'\nNeed to add: {len(additional_numbers)} numbers')
print(f'These additional numbers: {additional_numbers}')
print(f'Symmetric sequence: {sequence + additional_numbers}')


