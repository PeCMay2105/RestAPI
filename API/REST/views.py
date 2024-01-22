from django.shortcuts import render
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializer import Task_serializer


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
        return Response({'message': 'Task criada com sucesso'})
    else:
        return Response({'message': task.errors})
    
@api_view(['DELETE'])
def delTask(request):
    try:
        task = Task.objects.get(id=request.data['id'])
        task.delete()
        return Response({'message': 'Task deletada com sucesso'})
    except Exception as erro:
        return Response({'message': 'Erro ao deletar task/n'+ str(erro)})
    

@api_view(['GET','POST','DELETE'])
def task(request,primary_key):
    if request.method == 'GET':
        try:
            task = Task.objects.get(primary_key = primary_key)
            taskSerializada = Task_serializer(task)
            return Response(taskSerializada.data)
        except:
            return Response({'message': 'Nenhuma task com esse id foi encontrada'})
    elif request.method == 'POST':
        try:
            task = Task_serializer(data=request.data)
            if task.is_valid():
                task.save()
            else: raise Exception('A task passada possui valores inválidos')
        except:
            return Response()
    elif request.method == 'DELETE': 
        try:
            task = Task.objects.get(id=primary_key)
            task.delete()
        except:
            return Response({'message': 'Erro ao deletar task'})