from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rules', views.rules, name='rules'),
    path('api/simulation', views.simulation, name='simulation'),
]