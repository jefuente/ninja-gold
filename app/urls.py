from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('process_money', views.procesar),
    path('limpiar', views.limpiar),
]
