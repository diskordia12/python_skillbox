print('Task 2. Collectors')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор,
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.

# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50

# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.

# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

name = input('Enter your name: ')
credit = int(input('Enter amount of your debt: '))
money_for_credit= 0
print(f'{name}, your debt {credit} EUR')

while True:
    money_for_credit = int(input('How many EUR will you pay now to settle your debt? '))
    if money_for_credit >= credit:
        break
    print(f'Not enough, {name}. Let\'s again.')

print(f'Great, {name}! You paid off the debt. Thanks!')


