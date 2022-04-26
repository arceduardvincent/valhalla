from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets


router = DefaultRouter()

app_name = 'aws'

urlpatterns = [
    path('', include(router.urls)),
    path('virtualmachine/', viewsets.AWSVirtualMachineAPIList.as_view()),
    path('virtualmachine/<str:pk>/', viewsets.AWSVirtualMachineAPIDetail.as_view()),
]
