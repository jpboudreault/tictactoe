import random

from .cpu import Cpu
from .services import *
from game.transforms import *


class Random(Cpu):
    def name(self):
        return 'Random AI'

    def play(self, board: Board, player_side, opposing_side):
        # pick any spot that win, random is stupid but not that much
        winning_position = find_winning_position(board, player_side)
        if winning_position is not None:
            return winning_position

        possible_plays = []
        for i in range(9):
            if board.data[i] == ' ':
                possible_plays.append(i)

        return random.choice(possible_plays)
