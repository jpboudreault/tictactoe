from ai.ai import Ai
from game.transients import Board


class Xavier(Ai):
    def get_name(self):
        return 'Xavier''s AI 1.0'

    def play(self, board: Board, side):
        for line in board.get_rows():
            for i in range(3):
                if line.data[i] == ' ':
                    return line.positions[i]
        return None
