import random

from cpu.cpu import Cpu
from game.transients import Board


class First(Cpu):
    def name(self):
        return '1st Ai'

    def play(self, board: Board, player_side, opposing_side):
        for row in board.get_rows():
            for i in range(3):
                if row.data[i] == ' ':
                    return row.positions[i]
        return None
