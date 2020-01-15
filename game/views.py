import random

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .services import *
from .models import Game
from cpu.services import *


def about(request):
    return render(request, 'about.html')


def play(request):
    return render(request, 'play.html')


def rules(request):
    return render(request, 'rules.html')


def simulation(request):
    return render(request, 'simulation.html')


# No CSRF needed, there is no security on the website
@csrf_exempt
def games(request):
    if not request.POST:
        raise Exception('The API only supports POST')

    # asses that the CPU exists
    cpu = request.POST.get('cpu1', 'random')
    get_cpu(cpu)

    # create a game and make cpu play if needed
    cpu_first_player = random.choice([True, False])
    new_game = Game.objects.create(moves="[]", cpu_code=cpu, cpu_first_player=cpu_first_player)
    play_cpu1_if_needed(new_game)
    new_game.save()

    # return board
    return JsonResponse(game_response(new_game))


# No CSRF needed, there is no security on the website
@csrf_exempt
def move(request, game_id):
    if not request.method == 'POST':
        raise Exception('The API only supports POST')

    if not request.POST.get('move'):
        raise Exception('Invalid payload, move is mandatory')

    player_move = int(request.POST.get('move'))
    if player_move not in range(9):
        raise Exception('Invalid move, it must be between 0 and 8 got ' + str(player_move))

    existing_game = get_object_or_404(Game, pk=game_id)

    if existing_game.is_human_turn():
        existing_game.add_move(move)

    play_cpu1_if_needed(existing_game)
    existing_game.save()

    return JsonResponse(game_response(existing_game))


@csrf_exempt
def run_simulation(request):
    if not request.method == 'POST':
        raise Exception('The API only supports POST')

    code1 = request.POST.get('cpu1')
    cpu1 = get_cpu(code1)
    code2 = request.POST.get('cpu2')
    cpu2 = get_cpu(code2)

    games_response = []
    for i in range(20):
        cpu_first_player = random.choice([True, False])
        new_game = Game.objects.create(moves="[]", cpu_code=code1, cpu2_code=code2, cpu_first_player=cpu_first_player)
        new_game.save()

        try:
            while not game_2_board(new_game).is_game_over():
                if new_game.is_first_player_turn() != new_game.cpu_first_player:
                    cpu_turn = cpu2
                else:
                    cpu_turn = cpu1

                board = game_2_board(new_game)

                if new_game.is_first_player_turn():
                    cpu_move = cpu_turn.play(board, 'x', 'o')
                else:
                    cpu_move = cpu_turn.play(board, 'o', 'x')

                new_game.add_move(cpu_move)
        except Exception as e:
            print("An exception occurred: " + str(e))

        new_game.save()
        games_response.append(game_response(new_game))

    return JsonResponse(games_response, safe=False)


def game_response(game_model: Game):
    board = game_2_board(game_model)
    return {
        'id': game_model.id,
        'cpuCode': game_model.cpu_code,
        'cpu2Code': game_model.cpu2_code,
        'cpuFirstPlayer': game_model.cpu_first_player,
        'winningSide': board.get_winning_side(),
        'gameOver': board.is_game_over(),
        'data': board.data,
        'moves': game_model.get_moves(),
    }
