from game.transients import Board
from abc import ABCMeta, abstractmethod


class Ai:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_name(self): raise NotImplementedError

    @abstractmethod
    def play(self, board: Board, side): raise NotImplementedError
