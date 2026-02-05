from django.urls import path
from . import views

app_name = 'registre'

urlpatterns = [
    path('', views.registre, name='registre'),
    path('inici-sessio/', views.inici_sessio, name='inici_sessio'),
]
