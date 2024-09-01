"""
Задача 3. Регистрация
У вас есть файл с протоколом регистрации пользователей на сайте — registrations.txt.
Каждая строка содержит имя, имейл и возраст, разделённые пробелами.
Например: Василий test@test.ru 27.

Напишите программу, которая проверяет данные из файла для каждой строки:
- Присутствуют все три поля.
- Поле «Имя» содержит только буквы.
- Поле «Имейл» содержит @ и точку.
- Поле «Возраст» представляет число от 10 до 99.

В результате проверки сформируйте два файла:
- registrations_good.log для правильных данных; записывать строки как есть;
- registrations_bad.log — для ошибочных; записывать строку и вид ошибки.

Для валидации строки данных напишите функцию, которая может выдавать исключения:
- НЕ присутствуют все три поля: IndexError.
- Поле «Имя» содержит НЕ только буквы: NameError.
- Поле «Имейл» НЕ содержит @ и точку: SyntaxError.
- Поле «Возраст» НЕ представляет число от 10 до 99: ValueError.

Формат выходных данных
Содержимое файла registrations_bad.log:
Ольга kmrn@gmail.com 123        Поле «Возраст» НЕ представляет число от 10 до 99
Чехова kb@gmail.com 142        Поле «Возраст» НЕ представляет число от 10 до 99
……
Степан ky 59        Поле «Имейл» НЕ содержит @ и точку
……

Содержимое файла registrations_good.log:
Геннадий ttdababmt@gmail.com 69
Ольга ysbxur@gmail.com 20
……

Советы и рекомендации
- Помните, что пайтон не всегда будет выполнять операции, которые вы предполагали, например:
    if '1' and '2' in строка — по приоритету операций сперва будет выполнено действие с in,
    а уже потом and. Значит, пайтон не будет в этом случае искать 1 внутри строки.
- Элементы а, б, с: разделять объект (например, список) на несколько переменных очень удобно
    при помощи множественного присваивания.
    Но если элементов в списке окажется меньше, чем указанных переменных, то появится ошибка.
- При необходимости вы можете объединять исключения в except-блоке.
    Для этого нужно перечислить классы исключений, которые вы хотите отследить в кортеже:
    except (DrunkError, CarCrashError...) as exc
    As exc в данном случае сработает так же, как и с файлами в конструкции with open(...) as file.
    То есть пайтон запишет пойманное исключение в переменную с названием exc
    (название может быть любым).
- При переезде зачастую нужно вынести много коробок с вещами из дома.
    Если для переноса каждой коробки придётся открывать/закрывать двери, то на это уйдет много сил.
    Их уйдет меньше, если получится открыть двери один раз и закрыть, когда всё будет сделано.
    То же самое справедливо и для файлов. Старайтесь открывать и закрывать их экономно, например,
    открыть файлы можно до цикла, а закрыть — после
    (если нет необходимости переоткрывать файл внутри цикла).
"""


def validate_line(line: str):
    line_info = line.split()
    if len(line_info) != 3:
        raise IndexError('Not all three fields are present')
    name, e_mail, age = line_info
    if not age.isdigit():
        raise TypeError('Age contains not only digits')
    age = int(age)
    if not name.isalpha():
        raise NameError('The "Name" field contains NOT only letters')
    if '@' not in e_mail or '.' not in e_mail:
        raise SyntaxError('The "Email" field does NOT contain @ and dot')
    if age < 10 or age > 99:
        raise ValueError('The field "Age" DOES NOT represent a number from 10 to 99')

    return True


with open('registrations.txt', 'r', encoding='utf-8') as registrations_file, open('registrations_good.log', 'a', encoding='utf-8') as good_log_file, open('registrations_bad.log', 'a', encoding='utf-8') as bad_log_file:
    for line in registrations_file:
        try:
            validate_line(line)
        except (IndexError, NameError, SyntaxError, ValueError, TypeError) as e:
            bad_log_file.write(line[:-1] + '\t' + str(e) + '\n')
        else:
            good_log_file.write(line)






