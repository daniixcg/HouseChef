from django.urls import path
from . import views

app_name = 'receptes'

urlpatterns = [
    path('', views.receptes, name='receptes'),
]
