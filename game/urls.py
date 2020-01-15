from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('rules', views.rules, name='rules'),
    path('play', views.play, name='play'),
    path('simulation', views.simulation, name='simulation'),
    path('api/games', views.games),
    path('api/games/runSimulation', views.run_simulation),
    path('api/games/<int:game_id>/move', views.move),
]