from rest_framework import serializers

from .models import Logs


class LogSerializer(serializers.ModelSerializer):
    # user = serializers.Field(source='user.username')
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Logs
        fields = ('user', 'timestamp', 'data', 'notes', )
