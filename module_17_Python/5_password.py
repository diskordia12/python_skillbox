"""
Задание 5. Пароль
При регистрации на сайте, помимо логина, нужно придумать пароль.
Этот пароль должен состоять:
- минимум из восьми символов
- хотя бы одной большой буквы
- не менее трёх цифр.
Тогда он будет считаться надёжным.
Напишите программу, которая просит пользователя придумать пароль до тех пор,
пока этот пароль не станет надёжным. Должна использоваться латиница.

Пример
> Придумайте пароль: qwerty.
> Пароль ненадёжный. Попробуйте ещё раз.
> Придумайте пароль: qwerty12.
> Пароль ненадёжный. Попробуйте ещё раз.
> Придумайте пароль: qwerty123.
> Пароль ненадёжный. Попробуйте ещё раз.
> Придумайте пароль: qWErty123.
> Это надёжный пароль.
"""


def count_digits(password: str) -> bool:
    count_dgt = 0
    for sym in password:
        if sym.isdigit():
            count_dgt += 1
    return count_dgt >= 3


def is_upper(password: str) -> bool:
    password = list(password)
    for sym in password:
        if sym.isupper():
            return True
    return False


while True:
    password = input('Create a password: ')
    if len(password) < 8:
        print('Password is not secure. Try again')
        continue

    if not count_digits(password):
        print('Password is not secure. Try again')
        continue

    if not is_upper(password):
        print('Password is not secure. Try again')
        continue
    else:
        break

print('Password is secure')
