print('Задача 4. Калькулятор скидки')

# Васин друг переехал в новую квартиру, и ему нужно купить три стула в разные комнаты. Цены на стулья  разные, а в некоторых магазинах есть скидки. Друг хочет заказать у Васи калькулятор скидки, чтобы проще ориентироваться в ценах.

# Напишите программу, которая запрашивает три стоимости товара и вычисляет сумму чека. Если сумма чека превышает 10 000 руб., нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100). Итоговая сумма должна выводиться на экран.


first_chair_price = float(input('Enter the first chair price: '))
second_chair_price = float(input('Enter the second chair price: '))
third_chair_price = float(input('Enter the third chair price: '))
check_amount = first_chair_price + second_chair_price + third_chair_price

if check_amount > 10000:
    discount = check_amount * 10 / 100
    print(f'Total amount with discount: {check_amount - discount}')
else:
    print(f'Total amount: {check_amount}')





