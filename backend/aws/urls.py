from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets


router = DefaultRouter()
router.register('user', viewsets.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
