from django.shortcuts import render
from .models import Game

# Home
def home(request):
    return render(request, "html/home.html")

def payment(request):
    return render(request, "html/payment.html")


#Games
def games_all(request):
    games = Game.objects.all()
    return render(request, 'html/games/all.html', {'games': games})

def games_new(request):
    games = Game.objects.all()
    return render(request, 'html/games/new.html', {'games': games})

def games_popular(request):
    games = Game.objects.all()
    return render(request, 'html/games/popular.html', {'games': games})



#Console
def console_all(request):
    return render(request, 'html/console/all.html')

def console_new(request):
    return render(request, 'html/console/new.html')

def console_popular(request):
    return render(request, 'html/console/popular.html')


#components
def components_all(request):
    return render(request, 'html/components/all.html')

def components_new(request):
    return render(request, 'html/components/new.html')

def components_popular(request):
    return render(request, 'html/components/popular.html')
