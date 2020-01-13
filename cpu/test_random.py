from django.test import SimpleTestCase

from cpu.random import Random
from game.transforms import Board


def sample_input():
    return [
        'x', 'x', ' ',
        'o', ' ', ' ',
        'o', ' ', 'x',
    ]


class RandomAiTest(SimpleTestCase):

    def test_picks_random(self):
        data = sample_input()
        ai = Random()
        move = ai.play(Board(data), 'x', 'o')
        self.assertEquals(data[move], ' ')

    def test_get_name(self):
        ai = Random()
        self.assertRegex(ai.name().upper(), '.*RANDOM.*')
