from game.transforms import *


def get_cpu(code):
    if code == 'rand':
        from .random import Random
        return Random()
    elif code == 'xav':
        from .xavier import Xavier
        return Xavier()
    elif code == 'center':
        from .center import Center
        return Center()
    else:
        msg = "The cpu with the code %s could not be found" % code
        raise NotImplementedError(msg)


def find_winning_position(board: Board, side_to_match):
    for line in board.get_lines():
        if not line.is_filled():
            matches = find_matching_positions(board.data, line.get_positions(), side_to_match)
            if len(matches) == 2:
                return [item for item in line.get_positions() if item not in matches][0]
    return None


def find_matching_positions(data, positions, side_to_match):
    matches = []
    for p in positions:
        if data[p] == side_to_match:
            matches.append(p)

    return matches
