import random

from cpu.cpu import Cpu
from game.transients import Board


class Center(Cpu):
    def name(self):
        return 'Center AI 1.0'

    def play(self, board: Board, player_side, opposing_side):
        # pick any spot that win
        for line in board.get_lines():
            matches = self.find_matching_positions(board.data, line.get_positions(), player_side)
            if len(matches) == 2 and not line.is_filled():
                return [item for item in line.get_positions() if item not in matches][0]

        # pick any spot that would make the opponent win
        for line in board.get_lines():
            matches = self.find_matching_positions(board.data, line.get_positions(), opposing_side)
            if len(matches) == 2 and not line.is_filled():
                return [item for item in line.get_positions() if item not in matches][0]

        # pick middle
        if board.data[4] == ' ':
            return 4

        # pick corners first!
        possible_plays = self.find_matching_positions(board.data, [0, 2, 6, 8], ' ')
        if possible_plays:
            return random.choice(possible_plays)

        # pick any open spot left!
        possible_plays = self.find_matching_positions(board.data, [2, 3, 5, 7], ' ')
        if possible_plays:
            return random.choice(possible_plays)

        raise RuntimeError("Unreachable code")

    def find_matching_positions(self, data, positions, value_to_match):
        matches = []
        for p in positions:
            if data[p] == value_to_match:
                matches.append(p)

        return matches
