from django.urls import path
from Store import views

urlpatterns = [

    #Home Page
    path("", views.home, name="home"),

    #Payment
    path("payment.html", views.payment, name="payment"),


    #Game Page
    ## All
    path('games/all.html', views.games_all, name="games"),

    #Popular
    path('games/popular.html', views.games_popular, name="popular"),


    #Console Page
    ## All
    path('console/all.html', views.console_all, name="console"),

    #Popular
    path('console/popular.html', views.console_popular, name="popular"),
]
