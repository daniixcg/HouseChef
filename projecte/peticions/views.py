from django.shortcuts import render

def peticions(request):
    return render(request, 'peticions.html')
