from django.test import SimpleTestCase

from game.transients import Board


def sample_input():
    return [
        'x', 'x', ' ',
        'o', ' ', ' ',
        'o', ' ', 'x',
    ]


class GameTest(SimpleTestCase):

    def test_get_rows(self):
        lines = Board(sample_input()).get_rows()
        self.assertEqual(lines[0].get_data(), ['x', 'x', ' '])
        self.assertEqual(lines[0].get_positions(), [0, 1, 2])
        self.assertEqual(lines[1].get_data(), ['o', ' ', ' '])
        self.assertEqual(lines[1].get_positions(), [3, 4, 5])
        self.assertEqual(lines[2].get_data(), ['o', ' ', 'x'])
        self.assertEqual(lines[2].get_positions(), [6, 7, 8])

    def test_get_columns(self):
        columns = Board(sample_input()).get_columns()
        self.assertEqual(columns[0].get_data(), ['x', 'o', 'o'])
        self.assertEqual(columns[0].get_positions(), [0, 3, 6])
        self.assertEqual(columns[1].get_data(), ['x', ' ', ' '])
        self.assertEqual(columns[1].get_positions(), [1, 4, 7])
        self.assertEqual(columns[2].get_data(), [' ', ' ', 'x'])
        self.assertEqual(columns[2].get_positions(), [2, 5, 8])

    def test_get_diagonals(self):
        diagonals = Board(sample_input()).get_diagonals()
        self.assertEqual(diagonals[0].get_data(), ['x', ' ', 'x'])
        self.assertEqual(diagonals[0].get_positions(), [0, 4, 8])
        self.assertEqual(diagonals[1].get_data(), [' ', ' ', 'o'])
        self.assertEqual(diagonals[1].get_positions(), [2, 4, 6])

    def test_played_moves_count(self):
        played_moves = Board(sample_input()).played_moves_count()
        self.assertEqual(played_moves, 5)

    def test_get_lines(self):
        tuples = Board(sample_input()).get_lines()
        self.assertEqual(len(tuples), 8)

    def test_is_game_over(self):
        self.assertFalse(Board(sample_input()).is_game_over())

        all_x = ['x'] * 9
        self.assertTrue(Board(all_x).is_game_over())

    def test_get_winner(self):
        self.assertEquals(Board(sample_input()).get_winner(), None)

        all_x = ['x'] * 9
        self.assertEquals(Board(all_x).get_winner(), 'x')
