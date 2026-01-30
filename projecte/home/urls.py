from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.inici, name='inici'),
    path('cookies/', views.cookies, name='cookies'),
    path('privacitat/', views.privacitat, name='privacitat'),
]
