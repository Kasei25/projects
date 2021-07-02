board = [['-'] * 3 for i in range(3)]


def field():
    print('_______')
    print(f'  0 1 2')
    for i in range(3):
        rows = ' '.join(board[i])
        print(f'{i} {rows}')
    print('-------')


def input_check():
    while True:
        cord_str = input('Введите координаты хода:  ').split()
        if not cord_str:
            print('Не ввели')
            continue
        if len(cord_str) != 2:
            print('Ввели только одну координату')
            continue
        x, y = cord_str
        if not (x.isdigit()) or not (y.isdigit()):
            print('Введено(-ы) не численное(-ые) значение(-я)')
            continue
        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if board[x][y] != '-':
                print('Клетка занята')
                continue
        else:
            print('Ввели некорректные координаты. X и Y не могут быть < 0 или > 2 ')
            continue
        return x, y


def win_check():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('_______')
            print('Выиграл X')
            print('-------')
            return True
        if symbols == ['0', '0', '0']:
            print('_______')
            print('Выиграл 0')
            print('-------')
            return True
    return False


def versus_ai():
    print('__________________________________________________________________')
    print('Действие выполнить пока невозможно')
    print('------------------------------------------------------------------')
    print('                           ¯\_(ツ)_/¯                           ')
    input('Нажмите Enter для начала игры ')
    versus_human()


def versus_human():
    turn = 0
    while True:
        turn += 1
        field()
        if turn % 2 == 1:
            print('Ходит крестик')
        else:
            print('Ходит нолик')

        x, y = input_check()

        if turn % 2 == 1:
            board[x][y] = 'X'
        else:
            board[x][y] = '0'
        if win_check():
            break
        if turn == 9:
            print('_______')
            print('Ничья')
            print('-------')
            break


def game():
    while True:
        first_question = input('Вы хотите играть против виртуальной личности? (да/нет)  ')
        if first_question == 'да':
            versus_ai()
            break
        if first_question == 'нет':
            versus_human()
            break
        if first_question != 'да' and first_question != 'нет':
            print('Введите корректный ответ ')
            continue


game()