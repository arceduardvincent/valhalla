from rest_framework import permissions, viewsets
from .models import AWSVirtualMachine
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = AWSVirtualMachine.objects.all()
    model = AWSVirtualMachine
    permission_classes = [
        permissions.IsAuthenticated
    ]
