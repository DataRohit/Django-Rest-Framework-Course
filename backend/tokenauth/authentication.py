from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from tokenauth.models import ExpiringToken


class ExpiringTokenAuthentication(TokenAuthentication):
    model = ExpiringToken
    keyword = "Bearer"

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise AuthenticationFailed("Invalid token")

        if token.user.is_active and not token.has_expired():
            return token.user, token

        raise AuthenticationFailed("Token has expired or user is not active")
