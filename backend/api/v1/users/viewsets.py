from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import filters
from generic import views

from . import serializers

User = get_user_model()


class UserViewSet(views.APIModelViewSet):
    write_serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    model = User
    permission_classes = [
        permissions.IsAuthenticated
    ]
    filter_backends = (filters.SearchFilter,)
    search_fields = [
        'first_name', 'last_name', 'username',
    ]