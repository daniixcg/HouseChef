from django.shortcuts import render

def registre(request):
    return render(request, 'registre.html')

def inici(request):
    return render(request, 'inici.html')
