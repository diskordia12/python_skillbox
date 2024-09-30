"""
Задача 5. Счётчик
Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.

Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).
"""

from typing import Callable, Any
from functools import wraps


def counter(func: Callable) -> Callable:
    """
    Decorator that counts and outputs the number of calls to the decorated function
    :param func: The function to be decorated
    :return: Link to wrapper function
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapped_func.count += 1
        print(f'Function {func.__name__} was called {wrapped_func.count} times\n')
        return result

    wrapped_func.count = 0
    return wrapped_func


@counter
def test():
    print("test")


test()
test()
test()
