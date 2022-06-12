from django.urls import path

from .views import TodoListApiView, DetailTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path("", TodoListApiView.as_view()),
]
