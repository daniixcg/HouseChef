from django.urls import path
from . import views

app_name = 'peticions'

urlpatterns = [
    path('', views.peticions, name='peticions'),
]
