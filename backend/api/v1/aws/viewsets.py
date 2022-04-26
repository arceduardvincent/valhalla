from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from aws.models import AWSVirtualMachine
from django.http import Http404


class AWSVirtualMachineAPIList(APIView):

    def get(self, request):
        instances = AWSVirtualMachine.objects.all()
        serializer = serializers.AWSVirtualMachineSerializer(instances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.AWSVirtualMachineSerializer(data=request.data,
                                                             context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AWSVirtualMachineAPIDetail(APIView):

    def get_object(self, pk):
        try:
            return AWSVirtualMachine.objects.get(instance_id=pk)
        except AWSVirtualMachine.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instances = self.get_object(pk)
        serializer = serializers.AWSVirtualMachineSerializer(
            instances
        )
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = serializers.AWSVirtualMachineSerializer(
            instance, data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response({
                'data': data
            }
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
