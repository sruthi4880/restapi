from django.shortcuts import render
#./todo/views.py

from django.shortcuts import render
from rest_framework.response import Response
from . models import Todo
from . serializers import TodoSerializer
from rest_framework.views import APIView


# Create your views here.

class ListTodoAPIView(APIView):
    def get(self,request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

class TodoDetailAPIView(APIView):
    def get(self,request,pk):
        todos = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todos, many=False)
        return Response(serializer.data)

class CreateTodoAPIView(APIView):
    def post(self,request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateTodoAPIView(APIView):
    def post(self,request,pk):
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class DeleteTodoAPIView(APIView):
    def get(self,request,pk):
        todo = Todo.objects.get(id=pk)
        todo_instance = Todo.objects.get(id=pk)
        todo_instance.delete()
        return Response('Deleted')

# Create your views here.
