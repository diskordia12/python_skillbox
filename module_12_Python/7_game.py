"""Game
Вы пришли на работу в контору по разработке игр,
целевая аудитория которых - дети и их родители.

У прошлого программиста было задание
сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.

Однако программист, на место которого вы пришли
и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.

Используя этот шаблон,
реализуйте игры «Камень, ножницы, бумага» и «Угадай число».

Правила игры «Камень, ножницы, бумага»:
программа запрашивает у пользователя строку
и выводит, победил он или проиграл.

Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.

Правила игры “Угадай число”:
программа запрашивает у пользователя число до тех пор, пока он его не отгадает.
"""

import random

def rock_paper_scissors():
    # Здесь будет игра "Камень, ножницы, бумага"
    user_object = input('Enter rock or paper or scissors: ')

    rules = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    if user_object not in rules:
        print('Invalid option')
        return

    computer_choice = random.choice(list(rules.keys()))
    if user_object == computer_choice:
        print(f'Tie')
    elif user_object == rules[computer_choice]:
        print('You won')
    else:
        print('You lost')


def guess_the_number():
    # Здесь будет игра "Угадай число"
    computer_number = int(random.random() * 5)
    # computer_number = random.choice(range(100))
    try:
        user_number = int(input('Enter a number: '))
        if user_number == computer_number:
            print('You won')
        else:
            print('You lost')
    except ValueError:
        print('Error. You entered not a number')


def main_menu():
    # Здесь главное меню игры
    while True:
        choice = 0
        try:
            choice = int(input('1 - game "Rock, Paper, Scissors"\n'
                               '2 - play "Guess the number"\n'))
            if choice not in [1, 2]:
                raise ValueError('Invalid choice value')
        except ValueError:
            print('Error. Enter 1 or 2')
            continue
        except KeyboardInterrupt:
            exit(0)

        if choice == 1:
            rock_paper_scissors()
        else:
            guess_the_number()


main_menu()
