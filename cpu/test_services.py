from django.test import SimpleTestCase

from cpu.services import *
from cpu.random import Random


class ServicesTest(SimpleTestCase):

    def test_get_cpu_valie(self):
        cpu = get_cpu('rand')
        self.assertIsInstance(cpu, Random)

    def test_get_cpu_invalid(self):
        with self.assertRaises(NotImplementedError):
            get_cpu('invalid')

    def test_find_winning_position(self):
        data = [
            'x', ' ', 'o',
            'x', 'x', 'o',
            ' ', ' ', ' ',
        ]
        positions = find_winning_position(Board(data), 'x')
        self.assertEqual(positions, 6)

        positions = find_winning_position(Board(data), 'o')
        self.assertEqual(positions, 8)

    def test_find_matching_positions(self):
        x = 1
