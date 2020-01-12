from cpu.cpu import Cpu
from game.transients import Board


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

        winning_position = self.find_winning_position(board, player_side)
        if winning_position:
            return winning_position

        losing_position = self.find_winning_position(board, opposing_side)
        if losing_position:
            return losing_position


        if board.played_moves_count() == 4:

            return 5;

        return 5
    #
    # winning_position=self.find_winning_position
    # if winning_position:
    #     return winning_position

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