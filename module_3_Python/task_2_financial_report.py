print('Task 2. Financial report')

# Васе пришло очередное задание — автоматизация финансовой отчётности.
# Звучит сложно, а на деле нужно просто написать код, который будет считать нужные для отчёта вычисления автоматически.
# Вычисления, которые нужно реализовать в программе: сумму дохода первых двух кварталов поделить на сумму последних двух кварталов,
# чтобы понять динамику роста или падения дохода.

# Алгоритм действий в программе:
# 1) Запросить у пользователя четыре числа.
# 2) Отдельно сложить два первых и два вторых.
# 3) Разделить первую сумму на вторую.
# 4) Вывести результат на экран.

first_quarter_income = int(input('Enter the first quarter income:'))
second_quarter_income = int(input('Enter the second quarter income:'))
third_quarter_income = int(input('Enter the third quarter income:'))
fourth_quarter_income = int(input('Enter the fourth quarter income:'))

sum_first_and_second_quarter = first_quarter_income + second_quarter_income
sum_third_and_fourth_quarter = third_quarter_income + fourth_quarter_income

income_dynamics = sum_first_and_second_quarter / sum_third_and_fourth_quarter
print(f'Income dynamics: {income_dynamics}')


