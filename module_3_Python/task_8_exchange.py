print('Task 8. Exchange')

# Вы уже умеете менять местами строковые переменные и знаете,
# что в переменных кроме строк можно хранить и числа.
# Напишите программу, которая меняла бы значения двух переменных местами,
# но без использования третьей переменной и синтаксического сахара, который мы разбирали, а именно:
# без конструкции a, b = b, a. В переменные будут вводиться только числа.

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print(a, b)
# стереть эту строчку и вставить свой код здесь
a = a + b
b = a - b
a = a - b
print(a, b)

# Не изменяйте уже написанный код (input-ы и print-ы). Между принтами можно вставить столько строк кода, сколько вам нужно для решения.
