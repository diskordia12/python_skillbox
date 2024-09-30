"""
Задача 1. Функции
Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10:
def func_1(x):
    return x + 10

Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух
результатов переданной функции.
Пример основного кода:
print(func_2(func_1, 9))
Результат: 361.
"""
#
# from typing import Callable
#
#
# def func_2(func: Callable, *args, **kwargs) -> any:
#     return func(*args, **kwargs) * func(*args, **kwargs)
#
#
# def func_1(x):
#     return x + 10
#
#
# print(func_2(func_1, 9))

"""
Задача 2. Таймер
Вы работаете в отделе тестирования, и вам поручили с помощью различных функций
замерить скорость передачи данных на нескольких десятках сайтов.
Конечно же, вручную «щёлкать» сайты и замерять время вам было лень,
поэтому возникла идея написать «автотест», который всё сделает сам.

С помощью понятия функции высшего порядка реализуйте функцию-таймер,
которая замеряет время работы переданной функции func и выдаёт ответ на экран.
Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.
"""
#
# import time
# from typing import Callable, Any
#
#
# def timer(func: Callable, *args, **kwargs) -> Any:
#     start_at = time.time()
#     result = func(*args, **kwargs)
#     end_at = time.time()
#     print(f'Function ran for {round(end_at - start_at, 5)}')
#     return result
#
#
# def get_squares(number: int) -> int:
#     result = 0
#     for _ in range(1, number):
#         result += sum([num ** 2 for num in range(10000)])
#
#     return result
#
#
# my_result = timer(get_squares, 200)
# print(my_result)



"""
Задача 1. Двойной вызов
Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию.
Не забывайте про документацию и аннотации типов.

Пример декорируемой функции:
def greeting(name):
    print('Привет, {name}!'.format(name=name))

Основной код:
greeting('Tom')

Результат:
Привет, Tom!
Привет, Tom!
"""
# from typing import Callable, Any
#
#
# def do_twice(func) -> Callable:
#     def wrapped_func(*args, **kwargs) -> Any:
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapped_func
#
#
# @do_twice
# def greeting(name: str) -> None:
#     print('Привет, {name}!'.format(name=name))
#
#
# greeting('Tom')


"""
Задача 2. Таймер 2
Для замера времени передачи различных данных на множество сайтов вы написали специальную функцию,
которая сделала всю работу за вас, что позволило большую часть времени смотреть видео
с котиками в интернете. Однако, увидев свой код, вы как программист с опытом поняли,
что этот код можно написать намного красивее и удобнее.

Реализуйте декоратор, который замеряет время работы задекорированной функции
и выводит ответ на экран. Для проверки примените декоратор к какой-нибудь
«тяжеловесной» функции и вызовите её в основной программе.
"""
#
# import time
# from typing import Callable, Any
#
#
# def timer(func: Callable) -> Callable:
#     def wrapped_func(*args, **kwargs) -> Any:
#         start_at = time.time()
#         result = func(*args, **kwargs)
#         end_at = time.time()
#         print(f'Function ran for {round(end_at - start_at, 5)}')
#         return result
#     return wrapped_func
#
#
# @timer
# def get_squares(number: int) -> int:
#     result = 0
#     for _ in range(1, number):
#         result += sum([num ** 2 for num in range(10000)])
#     return result
#
#
# # my_result = get_squares(20)
# print(get_squares(20))


"""
Задача 1. Сэндвич
Есть функция, которая выводит начинку сэндвича.
Сверху и снизу от начинки идут различные ингредиенты вроде салата,
помидоров и других. Всё это в свою очередь содержится между двух половинок булочки.
Реализуйте такую функцию и два соответствующих декоратора — ингредиенты и хлеб.

Пример результата работы программы при вызове функции sandwich:
</----------\>
#помидоры#
--ветчина--
~салат~
<\______/>
"""

from typing import Callable, Any
import functools


def get_buns(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print('</----------\>')
        func(*args, **kwargs)
        print('<\______/>')

    return wrapped_func


def get_some_salade(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        print('#помидоры#')
        func(*args, **kwargs)
        print('~салат~')

    return wrapped_func


@get_buns
@get_some_salade
def sandwich(main_filling: str) -> None:
    """
    
    :param main_filling:
    :return:
    """
    print(f'--{main_filling}--')


sandwich('HAM')


"""
Задача 2. Плагины
Один проект состоит из огромного количества разнообразных функций,
часть из которых используется в других проектах в качестве плагинов,
то есть они как бы «подключаются» и создают дополнительный функционал.
Реализуйте специальный декоратор, который будет «регистрировать» нужные функции
как плагины и заносить их в соответствующий словарь. 
"""

from typing import Dict, Any, Callable
import functools


PLUGINS: Dict[str, Callable] = dict()


def register(func: Callable) -> Callable:
    """
    Decorator. Register a func like a plugin
    :param func: Callable
    :return: Callable
    """
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name: str) -> str:
    return f'Hello, {name}!'


print(PLUGINS)
print(say_hello('Tom'))
print(PLUGINS)

