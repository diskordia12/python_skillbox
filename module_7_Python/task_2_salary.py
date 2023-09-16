print('Task 2. Salary')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.

total_salary = 0

for month in range(0, 12):
    month_salary = int(input(f'Enter your {month + 1} month salary: '))
    total_salary += month_salary

print(f'Average annual salary of an employee is equal {total_salary/12}')

