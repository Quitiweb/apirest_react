from rest_framework import serializers

from .models import Profile


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('title', 'code', )
