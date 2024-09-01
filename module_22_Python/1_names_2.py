"""
Задача 1. Имена 2
Есть файл people.txt, в котором построчно хранится N имён пользователей.
Напишите программу, которая берёт количество символов в каждой строке файла
и в качестве ответа выводит общую сумму.
Если в какой-либо строке меньше трёх символов (не считая литерала \n),
то вызывается ошибка и сообщение, в какой именно строке она возникла.
Программа при этом не завершается и обрабатывает все имена файла.

Также при желании можно вывести все ошибки в отдельный файл errors.log.

Пример работы программы
Содержимое файла people.txt:
Василий
Николай
Надежда
Никита
Ян
Ольг
Евгения
Кристина

Ответ в консоли:
> Ошибка: менее трёх символов в строке 5.
> Общее количество символов: 49.
"""


def write_error(message: str):
    with open('errors.log', 'w') as errors_file:
        errors_file.write(f'Error: {message}')


def check_names_in_file(file_name: str) -> int:
    amount_of_sym = 0
    line_counter = 0
    with open(file_name, 'r') as people_file:
        for line in people_file:
            name = line.strip()
            line_counter += 1
            if len(name) < 3:
                write_error(f'{name} - line {line_counter} les that 3 symbols')
            amount_of_sym += len(name)
        return amount_of_sym


amount_of_symbols = check_names_in_file('people_2.txt')
print(f'Total amount of symbols: {amount_of_symbols}')

