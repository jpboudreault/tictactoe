from django.test import SimpleTestCase

from cpu.xavier import Xavier
from game.transients import Board


def sample_input():
    return


class RandomAiTest(SimpleTestCase):

    def test_picks_corner_on_start(self):
        data = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ',
        ]
        ai = Xavier()
        move = ai.play(Board(data), 'x', 'o')
        self.assertEquals(move, 0)

    def test_picks_opposing_corner_in_2nd(self):
        data = [
            'x', ' ', ' ',
            ' ', 'o', ' ',
            ' ', ' ', ' ',
        ]
        ai = Xavier()
        move = ai.play(Board(data), 'x', 'o')
        self.assertEquals(move, 8)

    def test_picks_another_corner_in_2nd(self):
        data = [
            'x', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', 'o',
        ]
        ai = Xavier()
        move = ai.play(Board(data), 'x', 'o')
        self.assertEquals(move, 6)
