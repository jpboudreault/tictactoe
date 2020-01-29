from django.urls import include, path

urlpatterns = [
    path(r'', include('game.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
