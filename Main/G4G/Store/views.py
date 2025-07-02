from django.shortcuts import render

# Home.
def home(request):
    return render(request, "html/home.html")

def payment(request):
    return render(request, "html/payment.html")

#Games
def games_all(request):
    return render(request, 'html/games/all.html')

def games_new(request):
    return render(request, 'html/games/new.html')

def games_popular(request):
    return render(request, 'html/games/popular.html')



#Console
def console_all(request):
    return render(request, 'html/console/all.html')

def console_new(request):
    return render(request, 'html/console/new.html')

#Console
def console_popular(request):
    return render(request, 'html/console/popular.html')
