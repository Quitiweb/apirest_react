from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.DeviceList.as_view(), name='device-list'),
    path('log/', views.LogList.as_view(), name='log-list'),
    path('user/', views.CurrentUser.as_view(), name='user-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
