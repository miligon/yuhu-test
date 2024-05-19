from django.urls import path, include

from rest_framework import routers

from .views import *
from .viewsets import *

route = routers.SimpleRouter()
route.register('api/tasks', TasksViewSet)

urlpatterns = route.urls + [
    path('tasks', TaskView.as_view(), name='list_tasks'),
    path('tasks/new/', create_task, name='create_task'),
    path('tasks/delete/<int:pk>', delete_task, name='delete_task'),
    path('tasks/edit/<int:pk>/', edit_task, name='edit_task'),
]