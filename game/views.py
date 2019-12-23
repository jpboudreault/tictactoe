from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi, welcome to the tic tac toe game")