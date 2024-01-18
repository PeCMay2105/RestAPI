from django.contrib import admin
from django.urls import path
from REST.views import listaTasks
from REST.views import criaTask


urlpatterns = [
    path('lista',listaTasks),
    path('task',criaTask)
]

