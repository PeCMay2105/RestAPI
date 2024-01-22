from django.contrib import admin
from django.urls import path
from REST.views import listaTasks
from REST.views import criaTask
from REST.views import task 
from REST.views import delTask


urlpatterns = [
    path('lista',listaTasks),
    path('task',criaTask),
    path('delete',delTask),
    path('<int:pk>',task)
]

