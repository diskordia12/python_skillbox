"""
Задача 1. Как дела?
Вася совсем заскучал на работе и решил побаловаться с кодом проекта.
Он написал надоедливый декоратор, который при вызове декорируемой функции спрашивает
у пользователя: «Как дела?», вне зависимости от ответа пишет что-то вроде:
«А у меня не очень!» — и только потом запускает саму функцию.
Правда, после такой выходки Васю чуть не уволили с работы.

Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.

Пример кода:
@how_are_you
def test():
    print('<Тут что-то происходит...>')
test()

Результат:
Как дела? Хорошо.
А у меня не очень! Ладно, держи свою функцию.
<Тут что-то происходит...>
"""

from typing import Callable, Any
from functools import wraps


def how_are_you(func: Callable) -> Callable:
    """
    Decorator, asks user every time before run a func
    Args:
        func: function for decoration.
    Returns: link to wrapped function.
    """

    @wraps(func)
    def wrapped_fun(*args, **kwargs) -> Any:
        """
        A wrapper for the decorated function that interacts with the user
        Args:
            *args: Positional arguments to be passed to the decorated function.
            **kwargs: Named arguments passed to the decorated function.
        Returns: The result returned by the decorated function
        """

        print('How are you? ')
        input('_')
        print('I\'m not doing so great. Fine, here is your function')
        result = func(*args, **kwargs)
        return result
    return wrapped_fun


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


test()
