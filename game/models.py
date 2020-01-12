from django.db import models


class Game(models.Model):
    moves = models.CharField(max_length=40)
    cpu_code = models.CharField(max_length=100)
    cpu_first_player = models.BooleanField()
    cpu2_code = models.CharField(max_length=100)
