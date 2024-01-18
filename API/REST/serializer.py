from rest_framework import serializers
from .models import Task
class Task_serializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo = serializers.CharField(max_length=100)
    completed = serializers.BooleanField()

    def create(self,validated_data):
        return Task.objects.create(**validated_data)