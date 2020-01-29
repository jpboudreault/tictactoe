from ast import literal_eval
from django.db import models


class Game(models.Model):
    moves = models.CharField(max_length=40)
    cpu_code = models.CharField(max_length=100)
    cpu_first_player = models.BooleanField()
    cpu2_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_move(self, move, raise_illegal_move=False):
        moves_list = self.get_moves()
        if move in moves_list:
            if raise_illegal_move:
                raise RuntimeError("Move %s already recorded in game %s" % (move, self.id))
            else:
                print("Move %s already recorded in game %s" % (move, self.id))
                return

        moves_list.append(move)
        self.moves = str(moves_list)

    def get_moves(self):
        return literal_eval(self.moves)

    def is_first_player_turn(self):
        return len(self.get_moves()) % 2 == 0

    #   human_turn    player_one_turn cpu_first
    #        F           F               F
    #        T           F               T
    #        T           T               F
    #        F           T               T
    def is_human_turn(self):
        player_one_turn = len(self.get_moves()) % 2 == 0
        return player_one_turn != self.cpu_first_player
