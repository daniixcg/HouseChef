from django.shortcuts import render

def inici(request):
    return render(request, 'home.html')

def cookies(request):
    return render(request, 'cookies.html')

def privacitat(request):
    return render(request, 'privacitat.html')

