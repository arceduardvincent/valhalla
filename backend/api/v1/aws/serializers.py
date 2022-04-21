from rest_framework import serializers
from django.contrib.auth import get_user_model
from aws.models import AWSVirtualMachine


class AWSVirtualMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = AWSVirtualMachine
        fields = '__all__'
