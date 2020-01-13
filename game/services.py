from ast import literal_eval

from .models import *
from cpu.services import *


def game_2_board(game: Game):
    # go from a list of moves to a data array ['x', ' ', 'o', ...]
    moves = literal_eval(game.moves)
    data = [' '] * 9
    for num, move in enumerate(moves, start=0):
        data[move] = 'x' if num % 2 == 0 else 'o'

    return Board(data)


def play_cpu_if_needed(game: Game):
    cpu = get_cpu(game.cpu_code)
    moves = literal_eval(game.moves)
    board = game_2_board(game)

    if board.is_game_over():
        return

    if game.cpu_first_player and len(moves) % 2 == 0:
        moves.append(cpu.play(board, 'x', 'o'))
    elif not game.cpu_first_player and len(moves) % 2 == 1:
        moves.append(cpu.play(board, 'o', 'x'))

    game.moves = "%s" % moves
