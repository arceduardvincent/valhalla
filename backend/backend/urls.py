"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import confirm_email

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('api.v1.users.urls')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/account-confirm-email/<str:key>/',
         confirm_email),
    path('api/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('aws/users/', include('aws.urls')),
    path('aws/auth/', include('rest_auth.urls')),
]

# swagger
api_info = openapi.Info(
    title="Valhalla API",
    default_version="v1",
    description="API documentation for Red Sound App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]
