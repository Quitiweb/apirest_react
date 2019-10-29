from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetDetail(APIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        codes = [snippet.code for snippet in Snippet.objects.filter(owner=request.user)]
        return Response(codes)
