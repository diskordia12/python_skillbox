# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

numbers_amount = int(input('Enter amount of numbers: '))


def get_digits_sum(n: int) -> int:
    summ = 0
    for digit in str(n):
        summ += int(digit)
    return summ


max_sum = 0
max_number = 0

for i in range(1, numbers_amount + 1):
    number = int(input(f'Enter {i} number: '))
    digit_sum = get_digits_sum(number)
    if digit_sum > max_sum:
        max_sum, max_number = digit_sum, number

print(f'The number with the largest sum of digits {max_number}'
      f' and the sum of digits: {max_sum}')
