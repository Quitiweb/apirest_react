import datetime
from django.utils.timezone import utc
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics, permissions, authentication
from rest_framework.response import Response

from .forms import CustomUserCreationForm
from .models import Logs
from .serializers import LogSerializer

now = datetime.datetime.utcnow().replace(tzinfo=utc)


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'landing/signup.html'


class LogDetail(generics.ListCreateAPIView):
    queryset = Logs.objects.all()
    serializer_class = LogSerializer
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        # data = [log.data for log in Logs.objects.filter(user=request.user)]
        queryset = Logs.objects.filter(user=request.user)
        serializer = LogSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        serializer.save(timestamp=now)
