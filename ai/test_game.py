from django.test import SimpleTestCase

from ai.first import First
from ai.random import Random
from ai.xavier import Xavier
from game.transients import Board


class RandomAiTest(SimpleTestCase):

    def test_play(self):
        ai1 = First()
        ai2 = Random()

        data = [' '] * 9

        while True:
            play = ai1.play(Board(data), 'o')
            print("player " + ai1.get_name() + ' plays ' + str(play))
            data[play] = 'o'

            if Board(data).is_game_over():
                break

            play = ai2.play(Board(data), 'x')
            print("player " + ai2.get_name() + ' plays ' + str(play))
            data[play] = 'x'

            if Board(data).is_game_over():
                break

        winner = Board(data).get_winner()
        if winner == 'x':
            winner_name = ai2.get_name()
        elif winner == 'o':
            winner_name = ai1.get_name()
        else:
            winner_name = 'None'
        print('>> game over, winner is "' + winner_name + '" <<')
        for row in range(3):
            print(data[0 + row*3] + ' ' +  data[1 + row*3] + ' ' + data[2 + row*3])
