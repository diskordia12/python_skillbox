"""
Задача 1. Ревью кода
Ваня работает middle-разработчиком на Python в IT-компании.
Один кандидат на позицию junior-разработчика прислал ему код тестового задания.
В задании был словарь из трёх студентов. Необходимо:
- Вывести на экран список пар «ID студента — возраст».
- Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения:
    - полный список интересов всех студентов
    - общую длину всех фамилий студентов.
Далее в основном коде вызывается функция, значения присваиваются отдельным переменным
и выводятся на экран.

Ваня — очень придирчивый программист, и после просмотра кода он понял,
что этого кандидата на работу не возьмёт, хотя код выдаёт верный результат.
Вот код кандидата:

students = {
1: {
'name': 'Bob',
'surname': 'Vazovski',
'age': 23,
'interests': ['biology, swimming']
},
2: {
'name': 'Rob',
'surname': 'Stepanov',
'age': 24,
'interests': ['math', 'computer games', 'running']
},
3: {
'name': 'Alexander',
'surname': 'Krug',
'age': 22,
'interests': ['languages', 'health food']
}
}

def f(dict):
lst = []
string = ''
for i in dict:
lst += (dict[i]['interests'])
string += dict[i]['surname']
cnt = 0
for s in string:
cnt += 1
return lst, cnt

pairs = []
for i in students:
pairs += (i, students[i]['age'])

my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)

Перепишите этот код так, чтобы он был максимально pythonic
и Ваня мало к чему мог придраться (только если очень захочется).
Убедитесь, что программа верно работает.
Проверки на существование записей в словаре не обязательны, но приветствуются.

Результат работы программы:
> Список пар «ID студента — возраст»: [(1, 23), (2, 24), (3, 22)]
> Полный список интересов всех студентов: {'running', 'computer games', 'math', 'languages', 'biology, swimming', 'health food'}
> Общая длина всех фамилий студентов: 20

"""


def get_students_interest_and_surname(students_data: dict) -> tuple:
    interests = set()
    surnames_length = 0

    for info in students_data.values():
        interests.update(info['interests'])
        surnames_length += (len(info['surname']))

    return interests, surnames_length


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

id_student_and_age = [(id_student, info_student['age'])
                      for id_student, info_student in students.items()]

# for id_student, info_student in students.items():
#     id_student_and_age.append((id_student, info_student['age']))

print(f'List of pairs "Student ID - age": {id_student_and_age}')

students_interests, surnames_len = get_students_interest_and_surname(students)
print(f'Full list of interests of all students: {students_interests}')
print(f'Total length of all students surnames: {surnames_len}')
