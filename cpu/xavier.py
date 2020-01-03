from cpu.cpu import Cpu
from game.transients import Board


class Xavier(Cpu):
    def name(self):
        return 'Xavier''s AI 1.0'

    def play(self, board: Board, player_side, opposing_side):
        empty = True
        for i in range(9):
            if board.data[i] == 'x' or board.data[i] == 'o':
                empty = False

        if empty:
            return 0
        if board.data[8] == ' ':
            return 8

        return 5
