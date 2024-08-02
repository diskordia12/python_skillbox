"""
Задание 6. Пицца
В базе данных интернет-магазина PizzaTime хранятся сведения о том, кто, что и сколько заказывал
у них в определённый период.
Вам нужно структурировать эту информацию и определить, сколько всего пицц купил каждый заказчик.
На вход в программу подаётся N заказов.
Каждый заказ представляет собой строку вида
«Покупатель — название пиццы — количество заказанных пицц».
Реализуйте код, который выводит список покупателей и их заказов по алфавиту.
Учитывайте, что один человек может заказать одну и ту же пиццу несколько раз.

Пример
> Введите количество заказов: 6
> Первый заказ: Иванов Пепперони 1
> Второй заказ: Петров Де-Люкс 2
> Третий заказ: Иванов Мясная 3
> Четвёртый заказ: Иванов Мексиканская 2
> Пятый заказ: Иванов Пепперони 2
> Шестой заказ: Петров Интересная 5
>
> Иванов:
> Мексиканская: 2
> Мясная: 3
> Пепперони: 3
>
> Петров:
> Де-Люкс: 2
> Интересная: 5
"""

amount_of_orders = int(input('Enter amount of orders: '))
orders = list()
structured_orders = dict()

for i_order in range(amount_of_orders):
    new_order = input(f'{i_order + 1}-order: ').split()
    orders.append(new_order)

    surname, pizza_name, number_of_pizzas = new_order
    if surname not in structured_orders:
        structured_orders[surname] = {pizza_name: int(number_of_pizzas)}
        continue

    if pizza_name not in structured_orders[surname]:
        structured_orders[surname].update({pizza_name: int(number_of_pizzas)})
    else:
        structured_orders[surname][pizza_name] += int(number_of_pizzas)


print(orders)
print(structured_orders)
print()

for name, order in sorted(structured_orders.items()):
    print(f'{name}:')
    for pizza_name, amount in sorted(order.items()):
        print(f'{pizza_name}: {amount}')
    print()
