"""
Задача 2. Замедление кода
В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
Типичный пример — функция, которая постоянно проверяет,
изменились ли данные на веб-странице или её код.
Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.
"""

from functools import wraps
from typing import Callable, Any
from time import sleep


def slowdown(func: Callable) -> Callable:
    """
    A decorator that slows down the execution of the decorated function by 5 seconds

    :param func: The function to be decorated
    :return: Link to wrapper function
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        """
        A wrapper for a decorated function that delays before calling.
        Delays execution for 5 seconds, then calls the original function
        with the arguments passed to it.

        :param args: Positional arguments passed to the decorated function
        :param kwargs: Named arguments passed to the decorated function
        :return: The result returned by the decorated function
        """
        sleep(5)
        print('Start')
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@slowdown
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


print(get_squares(4))

