from .models import Todo
from .serializers import TodoSerializer
# Create your views here.

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class TodoListApiView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
