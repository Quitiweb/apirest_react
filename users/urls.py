from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('device', views.DeviceViewSet, basename='device_list')
router.register('log', views.LogViewSet, basename='log_list')
router.register('user-info', views.CurrentUserViewSet, basename='user_list')

urlpatterns = [
    path('user/', include(router.urls)),
]
