from django.db import models
import copy


class Game(models.Model):
    def __init__(self, values, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = copy.deepcopy(values)

    def get_lines(self):
        return [
            [self.data[0], self.data[1], self.data[2], ],
            [self.data[3], self.data[4], self.data[5], ],
            [self.data[6], self.data[7], self.data[8], ],
        ]

    def get_columns(self):
        return [
            [self.data[0], self.data[3], self.data[6], ],
            [self.data[1], self.data[4], self.data[7], ],
            [self.data[2], self.data[5], self.data[8], ],
        ]

    def get_diagonals(self):
        return [
            [self.data[0], self.data[5], self.data[8], ],
            [self.data[2], self.data[5], self.data[6], ],
        ]

    def get_tuples(self):
        return self.get_lines().append(self.get_columns()).append(self.get_diagonals())

    def game_over(self):
        return False

    def is_winner(self):
        return False

    def save(self, *args, **kwargs):
        pass

    class Meta:
        managed = False
