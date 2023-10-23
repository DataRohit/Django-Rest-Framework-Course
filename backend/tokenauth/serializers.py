from django.utils import timezone
from rest_framework import serializers
from tokenauth.models import ExpiringToken
from rest_framework.authtoken.serializers import AuthTokenSerializer


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.UUIDField(read_only=True)


class ExpiringTokenSerializer(AuthTokenSerializer):
    class Meta:
        model = ExpiringToken
        fields = ("username", "password", "token")

    def create(self, validated_data):
        user = validated_data["user"]
        token, created = ExpiringToken.objects.get_or_create(user=user)
        if not created:
            expiration = timezone.now() + timezone.timedelta(days=1)
            token.expiration = expiration
            token.save()
        return token
