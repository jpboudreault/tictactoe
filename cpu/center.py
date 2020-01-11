import random

from cpu.cpu import Cpu
from game.transients import Board


class Center(Cpu):
    def name(self):
        return 'Center AI 1.0'

    def play(self, board: Board, player_side, opposing_side):
        # pick any spot that win
        winning_position = self.find_winning_position(board, player_side)
        if winning_position:
            return winning_position

        # pick any spot that would make the opponent win
        losing_position = self.find_winning_position(board, opposing_side)
        if losing_position:
            return losing_position

        # pick middle
        if board.data[4] == ' ':
            return 4

        # pick corners first!
        possible_moves = self.find_matching_positions(board.data, [0, 2, 6, 8], ' ')
        if possible_moves:
            return random.choice(possible_moves)

        # pick any open spot left!
        possible_moves = self.find_matching_positions(board.data, [1, 3, 5, 7], ' ')
        if possible_moves:
            return random.choice(possible_moves)

        raise RuntimeError('Nothing to play in board: %s' % board.data)

    def find_winning_position(self, board: Board, side_to_match):
        for line in board.get_lines():
            if not line.is_filled():
                matches = self.find_matching_positions(board.data, line.get_positions(), side_to_match)
                if len(matches) == 2:
                    return [item for item in line.get_positions() if item not in matches][0]
        return None

    def find_matching_positions(self, data, positions, side_to_match):
        matches = []
        for p in positions:
            if data[p] == side_to_match:
                matches.append(p)

        return matches
