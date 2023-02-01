from django.urls import path, include

from rest_framework.routers import DefaultRouter
from django.urls import path

from . import viewsets


router = DefaultRouter()
router.register("user", viewsets.UserViewSet, basename="user")

app_name = 'user'

urlpatterns = [
    path("", include(router.urls)),
]
