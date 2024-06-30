# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

numbers_amount = int(input('Enter amount of numbers: '))

sum_of_digits = 0
number_dgts = 0

def get_digits_sum(n: int) -> int:
    summ = 0
    for digit in str(n):
        summ += int(digit)
    return summ


for i in range(1, numbers_amount + 1):
    number = int(input(f'Enter {i} number: '))
    if get_digits_sum(number) > sum_of_digits:
        sum_of_digits = get_digits_sum(number)
        number_dgts = number

print(f'The number with the largest sum of digits {number_dgts}'
      f' and the sum of digits: {sum_of_digits}')
