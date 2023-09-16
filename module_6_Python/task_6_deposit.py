print('Задача 6. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

bank_deposit = int(input('Ваш текущий вклад: '))
percent = int(input('Процентная ставка: '))
bank_deposit_future = int(input('Сколько вы хотите накопить: '))
years = 0

while bank_deposit < bank_deposit_future:
    years += 1
    bank_deposit += (bank_deposit * percent)/100
    bank_deposit = int(bank_deposit)
print(f'Вы накопите за {years} лет')
