from rest_framework import permissions, authentication, generics
from rest_framework.response import Response

from .models import Profile
from .serializers import SnippetSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Profile.objects.filter(owner=self.request.user)
