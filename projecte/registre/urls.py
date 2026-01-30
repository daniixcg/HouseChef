from django.urls import path
from . import views

app_name = 'registre'

urlpatterns = [
    path('', views.registre, name='registre'),
    path('inici/',views.inici, name='inici'),
]
