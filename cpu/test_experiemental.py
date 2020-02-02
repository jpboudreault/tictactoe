from django.test import SimpleTestCase

from cpu.experimental import Experimental
from game.transforms import Board


def sample_input():
    return


class ExperimentalTest(SimpleTestCase):

    def test_picks_corner_on_start(self):
        data = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ',
        ]
        cpu = Experimental()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 0)

    def test_picks_opposing_corner_in_2nd(self):
        data = [
            'x', ' ', ' ',
            ' ', 'o', ' ',
            ' ', ' ', ' ',
        ]
        cpu = Experimental()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 8)

    def test_picks_another_corner_in_2nd(self):
        data = [
            'x', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', 'o',
        ]
        cpu = Experimental()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 6)

    def test_win_if_possible(self):
        data = [
            'x', ' ', 'o',
            ' ', ' ', ' ',
            'x', ' ', ' ',
        ]
        cpu = Experimental()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 3)

    def test_defend_if_possible(self):
        data = [
            'x', ' ', ' ',
            'o', ' ', 'o',
            ' ', 'x', ' ',
        ]
        cpu = Experimental()
        move = cpu.play(Board(data), 'x', 'o')
        self.assertEquals(move, 4)

    def test_defend_middle_if_free(self):
        data = [
            'x', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ',
        ]
        cpu = Experimental()
        move = cpu.play(Board(data), 'o', 'x')
        self.assertEquals(move, 4)

    def test_defend_corner_if_middle_taken(self):
        data = [
            ' ', ' ', ' ',
            ' ', 'x', ' ',
            ' ', ' ', ' ',
        ]
        cpu = Experimental()
        move = cpu.play(Board(data), 'o', 'x')
        self.assertEquals(move, 8)


    def test_pick_1(self):
        data = [
            'x', ' ', ' ',
            ' ', 'o', ' ',
            ' ', ' ', 'x',
        ]
        cpu = Experimental()
        move = cpu.play(Board(data), 'o', 'x')
        self.assertEquals(move, 1)