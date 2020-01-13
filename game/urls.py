from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('rules', views.rules, name='rules'),
    path('play', views.play, name='play'),
    path('simulate', views.simulate, name='simulate'),
    path('api/games', views.games, name='games'),
    path('api/games/<int:game_id>/move', views.move, name='move'),
]