from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('casa/<int:pk>/', views.visualizzaCasa, name="visualizza_casa"),
    path('registra/<int:pk>/', views.CreaCasa, name="crea_casa"),

]
