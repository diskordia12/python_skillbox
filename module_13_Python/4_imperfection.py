"""
Вы всё так же работаете в конторе по разработке игр и смотрите различные программы
прошлого горе-программиста.
В одной из игр для детей, связанной с мультяшной работой с числами,
вам нужно было написать код согласно следующим условиям:
программа получает на вход два числа;
в первом числе должно быть не менее трёх цифр,
во втором — не менее четырёх, иначе программа выдаёт ошибку.
Если всё нормально, то в каждом числе первая и последняя цифры меняются местами,
а затем выводится их сумма.

И тут вы натыкаетесь на программу,
которая была написана предыдущим программистом и которая как раз решает такую задачу.
Однако старший программист попросил вас немного переписать этот код,
чтобы он не выглядел так ужасно. Да и вам самим становится, мягко говоря, не по себе от него.

Постарайтесь разделить логику кода на три отдельные логические части (функции):
count_numbers — получает число и возвращает количество цифр в числе;
change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя, выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).

Разбейте приведённую ниже программу на функции.
Повторений кода должно быть как можно меньше.
Также сделайте, чтобы в основной части программы был только ввод чисел,
затем изменённые числа и вывод их суммы.


first_n = int(input("Введите первое число: "))
first_num_count = 0
temp = first_n

while temp > 0:
    first_num_count += 1
    temp = temp // 10

if first_num_count < 3:
    print("В первом числе меньше трёх цифр.")
else:
    last_digit = first_n % 10
    first_digit = first_n // 10 ** (first_num_count - 1)
    between_digits = first_n % 10 ** (first_num_count - 1) // 10
    first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
    print('Изменённое первое число:', first_n)
    second_n = int(input("\nВведите второе число: "))
    second_num_count = 0
    temp = second_n

    while temp > 0:
        second_num_count += 1
        temp = temp // 10
    if second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.")
    else:
        last_digit = second_n % 10
        first_digit = second_n // 10 ** (second_num_count - 1)
        between_digits = second_n % 10 ** (second_num_count - 1) // 10
        second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
        print('Изменённое второе число:', second_n)
        print('\nСумма чисел:', first_n + second_n)

"""


def count_digits(number: int) -> int:
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count


def change_number(number: int) -> int:
    digits = count_digits(number)
    last_digit = number % 10
    first_digit = number // 10 ** (digits - 1)
    between_digits = number % 10 ** (digits - 1) // 10
    number = last_digit * 10 ** (digits - 1) + between_digits * 10 + first_digit
    return number


def main():
    input_is_right = False
    while not input_is_right:
        try:
            first_number = int(input('Enter the first number: '))
            if count_digits(first_number) < 3:
                raise ValueError('The first number must be more than 3 digits!')

            second_number = int(input('Enter the second number: '))
            if count_digits(second_number) < 4:
                raise ValueError('The second number must be more than 4 digits!')

            input_is_right = True
        except ValueError as e:
            print(f'Error: {e}')

    changed_first_number = change_number(first_number)
    changed_second_number = change_number(second_number)
    print(f'Changed the first number: {changed_first_number}')
    print(f'Changed the second number: {changed_second_number}')
    print(f'Sum: {changed_first_number + changed_second_number}')


while True:
    try:
        main()
    except KeyboardInterrupt:
        exit(0)




