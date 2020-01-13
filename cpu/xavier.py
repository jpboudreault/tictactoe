from cpu.cpu import Cpu
from game.transforms import Board
from .services import find_winning_position


class Xavier(Cpu):
    def name(self):
        return 'Xavier''s AI 1.0'

    def play(self, board: Board, player_side, opposing_side):
        # board is empty
        if board.played_moves_count() == 0:
            return 0

        if board.played_moves_count() == 2:
            if board.data[8] == ' ':
                return 8
            else:
                return 6

        winning_position = find_winning_position(board, player_side)
        if winning_position:
            return winning_position

        losing_position = find_winning_position(board, opposing_side)
        if losing_position:
            return losing_position

        if board.played_moves_count() == 4:
            return 5;

        return 5
