"""
Задача 6. Крестики-нолики
Создайте программу, которая реализует игру «Крестики-нолики».
Для этого напишите:
1. Класс, который будет описывать поле игры.
class Board:
(Класс поля, который создаёт у себя экземпляры клетки)
- информация о состоянии поля (это может быть список из девяти элементов).
Методы:
    - «Изменить состояние клетки».
        Метод получает номер клетки и, если клетка не занята, меняет её состояние.
        Если состояние удалось изменить, метод возвращает True, иначе возвращается False.
    - «Проверить окончание игры».
        Метод не получает входящих данных, но возвращает True/False.
        True — если один из игроков победил, False — если победителя нет.

2. Класс, который будет описывать одну клетку поля:
class Cell:
- занята клетка или нет;
- номер клетки;
- символ, который клетка хранит (пустая, крестик, нолик).

3. Класс, который описывает поведение игрока:
class Player:
- имя,
- количество побед.

Метод:
- «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки).
    Введённый номер нужно обязательно проверить.

4. Класс, который управляет ходом игры:
class Game:
- состояние игры,
- игроки,
- поле.

Методы:
- Метод запуска одного хода игры.
    Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле,
    проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
- Метод запуска одной игры.
    Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков или ничьей.
    Если игра завершена, метод возвращает True, иначе False.
- Основной метод запуска игр.
    В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть.
    После каждой игры выводится текущий счёт игроков.
"""
import random


class Cell:

    def __init__(self):
        self.symbol = ''
        self.state = True    # True - vacant False - occupied

    def get_state(self):
        return self.state

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, sym: str):
        if not self.state:
            raise ValueError('Cell is occupied')
        self.state = False
        self.symbol = sym

    def clear(self):
        self.symbol = '-'
        self.state = True


class Player:

    def __init__(self, name: str, symbol: str, victory_amount=0):
        self.name = name
        self.symbol = symbol
        self.victory_amount = victory_amount

    def make_a_move(self):
        # Метод ничего не принимает и возвращает ход игрока (номер клетки).
        # Введённый номер нужно обязательно проверить.
        return int(input(f'{self.name} enter cell number: '))
        # return random.randint(1, 9)

    def add_victory(self):
        self.victory_amount += 1


class Board:

    def __init__(self):
        self.board = [Cell() for _ in range(9)]

    def __str__(self):
        res = '-------\n'
        for i in range(3):
            values = [cell.get_symbol() for cell in self.board[i * 3: (i + 1) * 3]]
            res += '|{}|{}|{}|\n'.format(*values)
        res += '-------'
        return res

    def change_cell_state(self, index: int, sym: str):
        if self.board[index - 1].get_state():
            self.board[index - 1].set_symbol(sym)
            return True
        return False

    def check_end_of_game(self):
        victory_combinations = [self.board[:3],
                                self.board[3:6],
                                self.board[6:],
                                self.board[::3],
                                self.board[1::3],
                                self.board[2::3],
                                self.board[::4],
                                self.board[2:7:2]
                                ]

        for comb in victory_combinations:
            if all([cell.get_symbol() == 'X' for cell in comb]):
                return True
            if all([cell.get_symbol() == '0' for cell in comb]):
                return True
        return False

    def clear(self):
        for cell in self.board:
            cell.clear()


class Game:

    def __init__(self, game_state, players: list, field: Board):
        self.game_state = game_state
        self.players = players
        self.field = field

    def run_one_move(self, player: Player):
        while True:
            cell_number = player.make_a_move()
            if self.field.board[cell_number - 1].get_state():
                break
            print('Cell is occupied')


        self.field.change_cell_state(cell_number, player.symbol)
        print(self.field)
        if self.field.check_end_of_game():
            player.add_victory()
            print(f'{player.name} won!\n')
            return True
        return False

    def run_one_game(self):
        self.field.clear()
        index = 0
        while not self.field.check_end_of_game():
            current_player = self.players[index]
            self.run_one_move(current_player)
            index = (index + 1) % 2

    def run_games(self):
        breaker = 0
        game_counter = 0
        while breaker != 1:
            game_counter += 1
            print(f'Game {game_counter}\n')
            self.run_one_game()
            print(f'{self.players[0].name} - {self.players[0].victory_amount} victories')
            print(f'{self.players[1].name} - {self.players[1].victory_amount} victories\n')

            breaker = int(input('0 - play one more\n'
                                '1 - stop\n'
                                'enter 0 or 1: '))


player_one = Player('Nick', 'X')
player_two = Player('Kate', '0')
players = [player_one, player_two]
my_field = Board()

my_game = Game(0, players, my_field)
my_game.run_games()










