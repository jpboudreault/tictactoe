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
    play_cpu_if_needed(new_game)
    new_game.save()

    # return board
    return JsonResponse(game_response(new_game))


# No CSRF needed, there is no security on the website
@csrf_exempt
def move(request, game_id):
    if not request.method == 'POST':
        raise Exception('The API only supports POST')

    player_move = request.POST.get('move')
    if not player_move:
        raise Exception('Invalid payload, move is mandatory')

    if player_move not in range(9):
        raise Exception('Invalid move, it must be between 0 and 8')

    existing_game = get_object_or_404(Game, pk=game_id)

    moves = literal_eval(existing_game.moves)
    if player_move not in moves:  # we should also check that it is the player turn
        moves.append(player_move)

    existing_game.moves = "%s" % moves

    play_cpu_if_needed(existing_game)
    existing_game.save()

    return JsonResponse(game_response(existing_game))


def game_response(game_model: Game):
    board = game_2_board(game_model)
    return {
        'id': game_model.id,
        'cpuCode': game_model.cpu_code,
        'cpuFirstPlayer': game_model.cpu_first_player,
        'winningSide': board.get_winning_side(),
        'gameOver': board.is_game_over(),
        'data': board.data,
        'moves': literal_eval(game_model.moves),
    }


def simulation(request):
    cpu1 = get_cpu(request.GET.get('cpu1', 'random'))
    cpu2 = get_cpu(request.GET.get('cpu2', 'random'))

    data = [' '] * 9
    moves = []
    first_player = random.choice([cpu1, cpu2])

    while True:
        board = Board(data)
        if board.is_game_over():
            if board.get_winning_side() == 'x':
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
        'cpu1Code': cpu1.name(),
        'cpu2Code': cpu2.name(),
        'winningSide': board.get_winning_side(),
        'data': board.data,
        'moves': moves,
    })
