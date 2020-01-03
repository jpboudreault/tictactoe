import random

from django.http import HttpResponse
from django.http import JsonResponse
from game.cpu_service import CpuService
from game.transients import Board


def index(request):
    return HttpResponse("Hi, welcome to the tic tac toe game")


def simulation(request):
    cpu_service = CpuService()
    cpu1 = cpu_service.get_ai(request.GET.get('cpu1', 'random'))
    cpu2 = cpu_service.get_ai(request.GET.get('cpu2', 'random'))

    data = [' '] * 9
    moves = []
    player = random.choice([cpu1, cpu2])

    while True:
        board = Board(data)
        if board.is_game_over():
            if board.get_winner() == 'x':
                print("> Game over! Winner is %s <" % cpu1.name())
            else:
                print("> Game over! Winner is %s <" % cpu2.name())

            print("History: %s" % moves)
            break

        if player == cpu2:
            player = cpu1
            side = 'x'
            other_side = 'o'
        else:
            player = cpu2
            side = 'o'
            other_side = 'x'

        move = player.play(board, side, other_side)

        if data[move] != ' ':
            raise Exception('Illegal move from %s, history: %s'.format((player.name(), moves)))

        data[move] = side
        moves.append(move)

    return JsonResponse({
        'cpu1': cpu1.name(),
        'cpu2': cpu2.name(),
        'winner': board.get_winner(),
        'data': board.data,
        'moves': moves,
    })
