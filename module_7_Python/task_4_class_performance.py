print('Task 4. Class performance')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

student_amount = int(input('Enter the number of students: '))
grade_a = 0
grade_b = 0
grade_c = 0

for student in range(0, student_amount):
    score = int(input(f'Enter the grade of the {student + 1} student: '))
    if score == 5:
        grade_a += 1
    elif score == 4:
        grade_b += 1
    else:
        grade_c += 1

if grade_a > grade_b and grade_a > grade_c:
    print(f'Today, the majority of students received a grade of 5')
elif grade_b > grade_a and grade_b > grade_c:
    print(f'Today, the majority of students received a grade of 4')
else:
    print(f'Today, the majority of students received a grade of 3')

