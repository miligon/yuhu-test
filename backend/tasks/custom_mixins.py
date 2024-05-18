from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class DisallowPatchMixin:
    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)