"""
Задача 2. Студенты
Реализуйте модель с именем Student, содержащую поля:
- «ФИ»,
- «Номер группы»,
- «Успеваемость» (список из пяти элементов).
Затем создайте список из десяти студентов (данные о студентах можете придумать
или запросить у пользователя)
и отсортируйте список по возрастанию среднего балла.
Выведите результат на экран.
"""

import random


class Student:

    def __init__(self, name: str, group: int, grades: list):
        self.name = name
        self.group_number = group
        self.performance = grades

    def get_average_grade(self):
        return sum(self.performance) / len(self.performance)

    def info(self):
        print(f'\nName: {self.name}\n'
              f'Group: {self.group_number}\n'
              f'Performance: {self.performance}')

    def __str__(self):
        return f'{self.name} {self.group_number}'


names = ['Kate', 'Nick', 'Liz', 'Jey', 'Sally', 'Bob', 'Tom', 'Monica', 'Rachel', 'Febe']

all_students = [Student(name,
                        random.randint(1, 10),
                        [random.randint(2, 5) for grade in range(5)])
                for name in names]

all_students_sorted = sorted(all_students, key=lambda student: student.get_average_grade())

# for person in all_students_sorted:
#     person.info()
#     print(person.get_average_grade())  # This only to be sure that sort went write

print(*all_students_sorted, sep='\n')





