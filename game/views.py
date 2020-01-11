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


def game(request, id):
    game = get_object_or_404(Game, pk=id)
    return JsonResponse({
    })


def game_response(game: Game):
    board = game_2_board(game)
    return {
        'id': game.id,
        'cpuCode': game.cpu_code,
        'cpuFirstPlayer': game.cpu_first_player,
        'winningSide': board.get_winning_side(),
        'gameOver': board.is_game_over(),
        'data': board.data,
        'moves': literal_eval(game.moves),
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
