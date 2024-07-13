from django.urls import path
from . import views

urlpatterns = [
    path('todos',views.todoList,name='todo-list'),
    path('todos/<int:pk>', views.todoDetails, name='todo-detail'),

    
]
