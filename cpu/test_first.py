from django.test import SimpleTestCase

from cpu.first import First
from game.transients import Board


def sample_input():
    return [
        'x', 'x', ' ',
        'o', ' ', ' ',
        'o', ' ', 'x',
    ]


class FirstAiTest(SimpleTestCase):

    def test_picks_first(self):
        data = sample_input()
        ai = First()
        move = ai.play(Board(data), 'x', 'o')
        self.assertEquals(move, 2)

    def test_get_name(self):
        ai = First()
        self.assertRegex(ai.name().upper(), '.*1ST.*')
