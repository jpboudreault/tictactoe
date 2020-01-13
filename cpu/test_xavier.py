from django.test import SimpleTestCase

from cpu.xavier import Xavier
from game.transforms import Board


def sample_input():
    return


class XavierTest(SimpleTestCase):

    def test_picks_corner_on_start(self):
        data = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ',
        ]
        cpu = Xavier()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 0)

    def test_picks_opposing_corner_in_2nd(self):
        data = [
            'x', ' ', ' ',
            ' ', 'o', ' ',
            ' ', ' ', ' ',
        ]
        cpu = Xavier()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 8)

    def test_picks_another_corner_in_2nd(self):
        data = [
            'x', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', 'o',
        ]
        cpu = Xavier()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 6)

    def test_win_if_possible(self):
        data = [
            'x', ' ', 'o',
            ' ', ' ', ' ',
            'x', ' ', ' ',
        ]
        cpu = Xavier()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 3)

    def test_defend_if_possible(self):
        data = [
            'x', ' ', ' ',
            'o', ' ', 'o',
            ' ', 'x', ' ',
        ]
        cpu = Xavier()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 4)
