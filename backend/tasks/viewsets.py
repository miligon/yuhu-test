from rest_framework import viewsets, mixins
from rest_framework.permissions import *
from .custom_mixins import DisallowPatchMixin
from .models import Tasks
from .serializer import TaskSerializer

class TasksViewSet(DisallowPatchMixin, mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    