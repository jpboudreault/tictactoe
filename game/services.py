from .models import *
from cpu.services import *


def game_2_board(game: Game):
    # go from a list of moves to a data array ['x', ' ', 'o', ...]
    data = [' '] * 9

    for num, move in enumerate(game.get_moves(), start=0):
        data[move] = 'x' if num % 2 == 0 else 'o'

    return Board(data)


def play_cpu1_if_needed(game: Game):
    cpu = get_cpu(game.cpu_code)
    board = game_2_board(game)

    if board.is_game_over() or game.is_human_turn():
        return

    if game.cpu_first_player:
        move = cpu.play(board, 'x', 'o')
    else:
        move = cpu.play(board, 'o', 'x')

    game.add_move(move)
