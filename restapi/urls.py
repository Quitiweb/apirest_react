"""restapi URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'QA API'
API_DESCRIPTION = 'A web API to configure and log profile devices'
schema_view = get_swagger_view(title=API_TITLE)


def react_frontend(request):
    return render(request, "public/index.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-docs/', schema_view),
    path('', include('profiles.urls')),
    path('', include('users.urls')),
    path('', react_frontend)
]
