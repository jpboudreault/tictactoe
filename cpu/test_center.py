from django.test import SimpleTestCase

from cpu.center import Center
from game.transforms import Board



class CenterAiTest(SimpleTestCase):

    def test_picks_center(self):
        data = [' '] * 9
        cpu = Center()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 4)

    def test_wins_if_possible(self):
        data = [
            ' ', ' ', ' ',
            'o', 'x', ' ',
            'o', ' ', 'x',
        ]
        cpu = Center()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 0)

    def test_defends_if_needed(self):
        data = [
            ' ', ' ', ' ',
            ' ', 'x', ' ',
            'o', ' ', 'x',
        ]
        cpu = Center()
        move = cpu.play(Board(data), 'o', 'x')
        self.assertEquals(move, 0)
