from django.urls import path
from Store import views

urlpatterns = [

    #Pagina Inicial
    path("", views.home, name="home"),
]
