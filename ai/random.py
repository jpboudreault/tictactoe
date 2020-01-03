import random

from ai.ai import Ai
from game.transients import Board


class Random(Ai):
    def name(self):
        return 'Random AI'

    def play(self, board: Board, player_side, opposing_side):
        possible_plays = []
        for i in range(9):
            if board.data[i] == ' ':
                possible_plays.append(i)

        return random.choice(possible_plays)
