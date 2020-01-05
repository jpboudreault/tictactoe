from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('rules', views.rules, name='rules'),
    path('play', views.play, name='play'),
    path('api/simulation', views.simulation, name='simulation'),
]