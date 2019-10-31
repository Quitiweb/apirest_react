from rest_framework import serializers

from .models import Logs, CustomUser


class LogSerializer(serializers.ModelSerializer):
    # user = serializers.Field(source='user.username')
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Logs
        fields = ('user', 'timestamp', 'data', 'notes', )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name',
                  'phone_number', 'address', 'personal_info',
                  'personal_info', 'subscription_type', 'payed', 'configuration',
                  'remoteLog', 'MACAddress')
