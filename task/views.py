from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_one(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update(request, id):
    task = Task.objects.get(id=id)
    if task:
        task.title = request.data['title']
        task.description = request.data['description']
        task.save()
    serializer = TaskSerializer(data=task)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['DELETE'])
def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response({"message": "delete done"})
