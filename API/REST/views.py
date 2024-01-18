from django.shortcuts import render
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from serializer import Task_serializer


def valida_task(receivedTask):
    try:
        task = Task.objects.get(id=receivedTask.data['id'])
        return True
    except:
        return False


@api_view(['GET'])
def listaTasks(request):
    tasks = Task.objects.all()
    lista = list(tasks.values())
    serialized_task = Task_serializer(tasks, many=True)
    return Response(serialized_task.data)

@api_view(['POST'])
def criaTask(request):
    task = Task_serializer(data=request.data)
    if task.is_valid():
        task.save()
    else:
        return Response({'message': 'Erro ao criar task'})
    
@api_view(['DELETE'])
def delTask(request):
    try:
        task = Task.objects.get(id=request.data['id'])
        task.delete()
    except Exception as erro:
        return Response({'message': 'Erro ao deletar task/n'+ str(erro)})
    

