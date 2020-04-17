import datetime

from django.utils.timezone import utc
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import permissions, authentication, viewsets, status, mixins

from .forms import CustomUserCreationForm
from .models import Logs, CustomUser, Device
from .serializers import LogSerializer, UserSerializer, DeviceSerializer

now = datetime.datetime.utcnow().replace(tzinfo=utc)


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'landing/signup.html'


class CurrentUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)
    http_method_names = ['get']

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(id=user.id)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.save(user=self.request.user)
        serializer.save(timestamp=now)

    def get_queryset(self):
        user = self.request.user
        return Device.objects.filter(user=user).all()


class LogViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        serializer.save(timestamp=now)

    def get_queryset(self):
        try:
            device_id = self.request.META['HTTP_DEVICE']
            if device_id == '0': # El front envia 0 al darle a 'All'
                queryset = Logs.objects.filter(device__user=self.request.user).all()
            else:
                queryset = Logs.objects.filter(device__id=device_id, device__user=self.request.user).all()
        except KeyError:
            queryset = Logs.objects.all()
        return queryset
