from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.inici, name='inici'),
    path('galetes/', views.galetes, name='galetes'),
    path('privacitat/', views.privacitat, name='privacitat'),
]
