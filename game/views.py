import random

from django.http import JsonResponse
from django.shortcuts import render

from game.cpu_service import CpuService
from game.transients import Board


def index(request):
    context = {
        'num_books': 1,
        'num_instances': 2,
        'num_instances_available': 3,
        'num_authors': 4,
    }

    return render(request, 'index.html', context)


def rules(request):
    return render(request, 'rules.html')


def simulation(request):
    cpu_service = CpuService()
    cpu1 = cpu_service.get_ai(request.GET.get('cpu1', 'random'))
    cpu2 = cpu_service.get_ai(request.GET.get('cpu2', 'random'))

    data = [' '] * 9
    moves = []
    first_player = random.choice([cpu1, cpu2])

    while True:
        board = Board(data)
        if board.is_game_over():
            if board.get_winner() == 'x':
                print('> Game over! Winner is %s <' % cpu1.name())
            else:
                print('> Game over! Winner is %s <' % cpu2.name())

            print('History: %s' % moves)
            break

        if len(moves) % 2 == 0:
            player = first_player
            side = 'x'
            other_side = 'o'
        else:
            player = [value for value in [cpu1, cpu2] if value not in [first_player]][0]
            side = 'o'
            other_side = 'x'

        move = player.play(board, side, other_side)

        if data[move] != ' ':
            raise Exception('Illegal move from %s, history: %s' % (player.name(), moves))

        data[move] = side
        moves.append(move)

    return JsonResponse({
        'cpu1': cpu1.name(),
        'cpu2': cpu2.name(),
        'winner': board.get_winner(),
        'data': board.data,
        'moves': moves,
    })
