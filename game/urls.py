from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('rules', views.rules, name='rules'),
    path('play', views.play, name='play'),
    path('api/games', views.games, name='games'),
    path('api/games/<int:id>', views.game, name='game'),
    path('api/simulation', views.simulation, name='simulation'),
]