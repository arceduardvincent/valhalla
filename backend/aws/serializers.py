from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AWSVirtualMachine
        fields = '__all__'
