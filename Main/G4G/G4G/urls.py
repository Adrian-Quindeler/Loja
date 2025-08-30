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

    #New
    path('games/new.html', views.games_new, name="new"),

    #Popular
    path('games/popular.html', views.games_popular, name="popular"),


    #Console Page
    ## All
    path('console/all.html', views.console_all, name="console"),

    # New
    path('console/new.html', views.console_new, name="new"),

    #Popular
    path('console/popular.html', views.console_popular, name="popular"),


    #Components Page
    ## All
    path('components/all.html', views.components_all, name="components"),

    # New
    path('components/new.html', views.components_new, name="new"),

    #Popular
    path('components/popular.html', views.components_popular, name="popular"),
]
