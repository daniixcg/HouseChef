from django.shortcuts import render

def faqs(request):
    return render(request, 'faqs.html')
