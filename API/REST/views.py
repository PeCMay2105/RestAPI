from django.shortcuts import render
from .models import Task
from django.http import JsonResponse


def listaTasks(request):
    tasks = Task.objects.all()
    lista = list(tasks.values())
    return JsonResponse({
        'data': lista
    })