from board import Board


def _next_player(current_player: int):
    return 2 if current_player == 1 else 1


def _print_board_status(board):
    print('Board status:\n' + str(board))


if __name__ == '__main__':
    player_dict = {1: Board.CIRCLE, 2: Board.CROSS}
    current_player = 1

    board = Board()
    _print_board_status(board)
    while True:
        position = input(f"Player {current_player}'s ({player_dict[current_player]}) turn. Input position (for example, a1): ")
        if not board.set_position(position, player_dict[current_player]):
            print('Wrong position, please input a position in this format: b2')
            continue

        if board.is_win(position):
            _print_board_status(board)
            print(f'Player {current_player} WINS!')
            break
        elif board.is_full():
            _print_board_status(board)
            print("It's a tie! :(")
            break

        current_player = _next_player(current_player)
        _print_board_status(board)
