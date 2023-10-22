from django.utils import timezone
from restapi.models import ExpiringToken
from rest_framework.authtoken.serializers import AuthTokenSerializer


class ExpiringTokenSerializer(AuthTokenSerializer):
    class Meta:
        model = ExpiringToken
        fields = ("username", "password", "token")

    def create(self, validated_data):
        user = validated_data["user"]
        token, created = ExpiringToken.objects.get_or_create(user=user)
        if not created:
            expiration = timezone.now() + timezone.timedelta(minutes=2)
            token.expiration = expiration
            token.save()
        return token
