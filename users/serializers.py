from rest_framework import serializers

from .models import Logs, CustomUser, Device


class LogSerializer(serializers.ModelSerializer):
    # user = serializers.Field(source='user.username')
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    device = serializers.SlugRelatedField(slug_field='id', read_only=True)
    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Logs
        fields = ('user', 'timestamp', 'data', 'notes', 'device')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password', 'is_superuser', 'groups', 'user_permissions')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
