"""
Задача 3. Логирование
Реализуйте декоратор logging, который будет отвечать за логирование функций.
На экран выводится название функции и её документация.
Если во время выполнения декорируемой функции возникла ошибка,
то в файл function_errors.log записывается название функции и ошибки.

Постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки,
а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.

Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime
"""
from typing import Callable, Any
from functools import wraps
from datetime import datetime


def logger(func: Callable) -> Callable:
    """

    :param func:
    :return:
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:

        try:
            print(f'Name of the function: {func.__name__}')
            print(f'Documentation: {func.__doc__}')
            result = func(*args, **kwargs)
            print()
            return result
        except Exception as e:
            print(f'Error calling function {func.__name__}')
            with open('function_errors.log', 'a+') as file:
                file.write(f'Function: {func.__name__}, Error: {str(e)}, time: {datetime.now()}\n')

    return wrapped_func


@logger
def test() -> None:
    """
    Just function with error
    :return:
    """
    print('<Тут что-то происходит...>')
    print(5/0)


@logger
def varname() -> None:
    """Присвоим не существующую переменную"""
    x = y


@logger
def get_squares(number: int) -> int:
    """
    Functions for get sum of squares of a number

    :param number:  a number up to count squares
    :return:  sum of squares
    """
    result = 0
    for _ in range(1, number):
        result += sum([num ** 2 for num in range(100)])
    return result


print(test())
print(get_squares(4))
varname()
