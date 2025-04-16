from django.urls import path
from Store import views

urlpatterns = [

    #Pagina Inicial
    path("", views.home, name="home"),

    #Pagina de Jogos
    path('games.html', views.games, name="games"),
]
