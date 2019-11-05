from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('log/', views.LogDetail.as_view(), name='log-detail'),
    path('user/', views.CurrentUser.as_view(), name='user-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
