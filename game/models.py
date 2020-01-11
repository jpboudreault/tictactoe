from django.db import models


class Game(models.Model):
    moves = models.CharField(max_length=9)
    cpu_name = models.CharField(max_length=100)
    cpu_first_player = models.BooleanField()
