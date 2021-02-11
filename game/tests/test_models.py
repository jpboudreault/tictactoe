from django.test import TestCase

from game.models import Game


class ModelsTest(TestCase):
    def setUp(self):
        Game.objects.create(cpu_first_player=False, cpu_code='rand', moves='[1,2]')

    def test_get_moves(self):
        game = Game.objects.first()
        self.assertEqual(game.get_moves(), [1, 2])

    def test_add_move(self):
        game = Game.objects.first()
        game.add_move(8)
        self.assertEqual(game.get_moves(), [1, 2, 8])

    def test_add_move_existing(self):
        game = Game.objects.first()
        game.add_move(1)
        self.assertEqual(game.get_moves(), [1, 2])

    def test_is_first_player_turn(self):
        game = Game.objects.first()
        self.assertTrue(game.is_first_player_turn())
