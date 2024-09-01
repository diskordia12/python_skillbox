"""
Задача 4. Чат
Что нужно сделать
Реализуйте программу — чат, в котором могут участвовать сразу несколько человек,
то есть программу, которая может работать одновременно для нескольких пользователей.
При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
- Посмотреть текущий текст чата.
- Отправить сообщение (затем вводит сообщение).
Действия запрашиваются бесконечно.
Примечание: для решения задачи вам достаточно текущих знаний,
нужно лишь проявить немного фантазии и хитрости.
Не углубляйтесь в дебри работы с сетями, создание GUI-приложений и прочее.
Однако, если очень хочется, то останавливать вас никто не будет!
"""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


with open('chat.txt', 'w+', encoding='utf-8') as chat_file:
    while True:
        user_name = input('Your name: ')

        choice = input('1 - Look into the chat\n'
                       '2 - write a message\n'
                       'enter digit_choice: ')

        print()
        if choice == '1':
            chat_file.seek(0)
            for line in chat_file:
                pos = line.find(':')
                nick, message = line[:pos], line[pos + 2:]
                fmt = '\t\t{}\n\t\t{}' if user_name == nick else '{}\n{}'
                print(fmt.format(bcolors.OKCYAN + nick + bcolors.ENDC,
                                 bcolors.OKGREEN + message + bcolors.ENDC))
                # if user_name in line:
                #     print('\t\t{}\n\t\t{}'.format(nick, nick), end='')
                # else:
                #     print('{}\n{}'.format(line[:pos], line[pos + 2:]), end='')
        elif choice == '2':
            user_message = input('Your message: ')
            chat_file.write(user_name + ': ' + user_message + '\n')
        else:
            print('Enter 1 or 2 for choice')
