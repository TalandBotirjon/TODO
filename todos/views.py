from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.

from rest_framework.generics import ListAPIView, RetrieveAPIView

class TodoListApiView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
