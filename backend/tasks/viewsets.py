from rest_framework import viewsets
from rest_framework.permissions import *

from .models import *
from .serializer import *

class TasksViewSet(viewsets.ModelViewSet):
    #permission_classes = [DjangoModelPermissions]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer