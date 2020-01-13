import random

from .cpu import Cpu
from .services import find_winning_position, find_matching_positions
from game.transforms import Board


class Center(Cpu):
    def name(self):
        return 'Center AI 1.0'

    def play(self, board: Board, player_side, opposing_side):
        # pick any spot that win
        winning_position = find_winning_position(board, player_side)
        if winning_position:
            return winning_position

        # pick any spot that would make the opponent win
        losing_position = find_winning_position(board, opposing_side)
        if losing_position:
            return losing_position

        # pick middle
        if board.data[4] == ' ':
            return 4

        # pick corners first!
        possible_moves = find_matching_positions(board.data, [0, 2, 6, 8], ' ')
        if possible_moves:
            return random.choice(possible_moves)

        # pick any open spot left!
        possible_moves = find_matching_positions(board.data, [1, 3, 5, 7], ' ')
        if possible_moves:
            return random.choice(possible_moves)

        raise RuntimeError('Nothing to play in board: %s' % board.data)
