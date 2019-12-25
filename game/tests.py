from django.test import SimpleTestCase

from game.models import Game


class GameTest(SimpleTestCase):
    def test_get_lines(self):
        inputs = [
            'x', 'x', ' ',
            'o', ' ', ' ',
            'o', ' ', 'x',
        ]
        board = Game(inputs)
        lines = board.get_lines()
        self.assertEqual(lines[0], ['x', 'x', ' '])
        self.assertEqual(lines[1], ['o', ' ', ' '])
        self.assertEqual(lines[2], ['o', ' ', 'x'])

    def test_get_columns(self):
        inputs = [
            'x', 'x', ' ',
            'o', ' ', ' ',
            'o', ' ', 'x',
        ]
        board = Game(inputs)
        columns = board.get_columns()
        self.assertEqual(columns[0], ['x', 'o', 'o'])
        self.assertEqual(columns[1], ['x', ' ', ' '])
        self.assertEqual(columns[2], [' ', ' ', 'x'])

    def test_get_diagonals(self):
        inputs = [
            'x', 'x', ' ',
            'o', ' ', ' ',
            'o', ' ', 'x',
        ]
        board = Game(inputs)
        diagonals = board.get_diagonals()
        self.assertEqual(diagonals[0], ['x', ' ', 'x'])
        self.assertEqual(diagonals[1], [' ', ' ', 'o'])
