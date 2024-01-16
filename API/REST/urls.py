from django.contrib import admin
from django.urls import path
from REST.views import listaTasks


urlpatterns = [
    path('lista',listaTasks)
]

