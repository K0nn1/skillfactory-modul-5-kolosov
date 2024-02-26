board = list(range(1, 10))
board_size = 3
def draw_board():
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * board_size], '|', board[1 + i *board_size], '|', board[2 + i *board_size], '|')
        print(('_' * 3 + '|') * 3)

def game_step(index, char):
    if index > 9 or index < 1 or board[index - 1] in ('X', 'O'):
        return False

    board[index - 1] = char
    return True


def check_win():
    win = False

    win_comb = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )
    for pos in win_comb:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]
    return win

def game_start():
    current_player = 'X'
    step = 1
    draw_board()

    while step < 10 and check_win() == False:

        while True:
            index = input('Ход игрока ' + current_player + '. Введите номер поля (0 для выхода): ')
            try:
                index = int(index)
                break
            except ValueError:
                print('Не верное значение! Попробуйте снова.')


        if int(index) == 0:
            print(f'Игрок {current_player} отказался продолжить. Игра окончена.')
            break

        if game_step(int(index), current_player):
            print('')

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            step += 1
        else:
            print('Неверный номер! Повторите ход.')
    if step == 10:
        print('Ничья!')
    else:
        print('Победа ' + check_win())



game_start()
