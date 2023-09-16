print('Task 6. Deposit')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

bank_deposit = int(input('Your current deposit: '))
percent = int(input('interest rate: '))
bank_deposit_future = int(input('How much would you like to save: '))
years = 0

while bank_deposit < bank_deposit_future:
    years += 1
    bank_deposit += (bank_deposit * percent)/100
    bank_deposit = int(bank_deposit)
print(f'You will accumulate the desired amount for {years} years')
