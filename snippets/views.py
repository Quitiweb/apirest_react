from rest_framework import permissions, authentication, generics
from rest_framework.response import Response

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetDetail(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Snippet.objects.filter(owner=self.request.user)
