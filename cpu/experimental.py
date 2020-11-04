import random

from cpu.cpu import Cpu
from game.transforms import Board
from .services import find_winning_position


# Author: Xavier
class Experimental(Cpu):
    def name(self):
        return 'Xavier''s AI 1.0'

    def play(self, board: Board, player_side, opposing_side):

        winning_position = find_winning_position(board, player_side)
        if winning_position is not None:
            return winning_position

        losing_position = find_winning_position(board, opposing_side)
        if losing_position is not None:
            return losing_position

        # board is empty
        if board.played_moves_count() == 0:
            return 0

        if board.played_moves_count() == 2:
            if board.data[8] == ' ':
                return 8
            else:
                return 6

        if board.played_moves_count() == 4:
            if board.data[0] == player_side and board.data[6] == player_side:
                return 2
            else:
                raise RuntimeError("Not reachable")

        if board.played_moves_count() == 1:
            if board.data[4] == opposing_side:
                return 8
            else:
                return 4
        if board.played_moves_count() == 3:
            if board.data[0] == opposing_side and board.data[8] == opposing_side:
                return 1
            if board.data[2] == opposing_side and board.data[6] == opposing_side:
                return 1
            if board.data[2] == opposing_side and board.data[6] == opposing_side:
                return 1
            if board.data[4] == opposing_side and board.data[0] == opposing_side:
                return 2
            if board.data[1] == opposing_side and board.data[5] == opposing_side:
                return 2
            if board.data[1] == opposing_side and board.data[3] == opposing_side:
                return 0
            if board.data[5] == opposing_side and board.data[7] == opposing_side:
                return 8
            if board.data[3] == opposing_side and board.data[7] == opposing_side:
                return 6
            if board.data[1] == opposing_side and board.data[8] == opposing_side:
                return 2
            if board.data[2] == opposing_side and board.data[7] == opposing_side:
                return 8
            if board.data[2] == opposing_side and board.data[3] == opposing_side:
                return 0
            if board.data[0] == opposing_side and board.data[5] == opposing_side:
                return 2
            if board.data[1] == opposing_side and board.data[6] == opposing_side:
                return 0
            if board.data[0] == opposing_side and board.data[7] == opposing_side:
                return 6
            if board.data[3] == opposing_side and board.data[8] == opposing_side:
                return 6
            if board.data[6] == opposing_side and board.data[5] == opposing_side:
                return 8
        if board.played_moves_count() == 5:
            if board.data[1] == opposing_side and board.data[3] == opposing_side and board.data[0] == ' ':
                return 0
            if board.data[1] == opposing_side and board.data[5] == opposing_side and board.data[2] == ' ':
                return 2
            if board.data[3] == opposing_side and board.data[7] == opposing_side and board.data[6] == ' ':
                return 6
            if board.data[5] == opposing_side and board.data[7] == opposing_side and board.data[8] == ' ':
                return 8
        possible_plays = []
        for i in range(9):
            if board.data[i] == ' ':
                possible_plays.append(i)

        return random.choice(possible_plays)
