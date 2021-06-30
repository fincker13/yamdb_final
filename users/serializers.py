from rest_framework import serializers

from .models import User


class ConfirmationSerializer(serializers.Serializer):
    """Serialize отправки кода кодтверждения и регистраци"""
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')


class AuthSerializer(serializers.Serializer):
    """Serializer аутентификации"""
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    """Serializer пользователя"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'bio', 'email', 'role')
