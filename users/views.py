import datetime
from django.utils.timezone import utc
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import mixins, viewsets
from rest_framework.exceptions import NotFound
from .forms import CustomUserCreationForm
from .models import Logs, CustomUser, Device
from .serializers import LogSerializer, UserSerializer, DeviceSerializer

now = datetime.datetime.utcnow().replace(tzinfo=utc)


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'landing/signup.html'


class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        head_token = request.META.get('HTTP_USER')
        print(head_token)
        token = Token.objects.filter(key=head_token).first()
        print('token: ' + str(token))
        if token is not None:
            print('user: ' + str(token.user))
            queryset = Device.objects.filter(user=token.user).all()
            serializer = DeviceSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.user.is_authenticated:
            queryset = Device.objects.filter(user=request.user).all()
            serializer = DeviceSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({
                'status': 'Bad request',
                'message': 'Please provide an user token to retrieve the data',
                'errors': 'NO_AUTH_USER'  # for example
            }, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        serializer.save(timestamp=now)


class LogList(generics.ListCreateAPIView):
    queryset = Logs.objects.all()
    serializer_class = LogSerializer

    def get(self, request, *args, **kwargs):
        head_token = request.META.get('HTTP_USER')
        device = request.META.get('HTTP_DEVICE')
        print(head_token)
        token = Token.objects.filter(key=head_token).first()
        print('token: ' + str(token))
        if token is not None:
            if device and device != '0':
                queryset = Logs.objects.filter(device__id=device, device__user=token.user).all()
            else:
                queryset = Logs.objects.filter(device__user=token.user).all()
            serializer = LogSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.user.is_authenticated:
            if device and device != '0':
                queryset = Logs.objects.filter(device__id=device, device__user=request.user).all()
            else:
                queryset = Logs.objects.filter(device__user=request.user).all()
            serializer = LogSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            print('iii')
            return Response({
                'status': 'Bad request',
                'message': 'Please provide an user token to retrieve the data',
                'errors': 'NO_AUTH_USER'  # for example
            }, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        serializer.save(timestamp=now)


class CurrentUser(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(id=user.id)
